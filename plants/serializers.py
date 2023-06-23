from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import (

    Vestiging, 
    Energie_import,
    Energie_export,
    Project,
    Project_kerngetallen,

)



class VestigingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vestiging
        fields = "__all__"

class Energie_importSerializer(serializers.ModelSerializer):
    vestigingnaam = serializers.ReadOnlyField(source="vestiging.vestigingnaam")
    lattitude = serializers.ReadOnlyField(source="vestiging.lattitude")
    longitude = serializers.ReadOnlyField(source="vestiging.longitude")
    belangenvereniging = serializers.ReadOnlyField(source="vestiging.bedrijf.belangenvereniging")
    sector = serializers.ReadOnlyField(source="vestiging.bedrijf.sector")

    class Meta:
        model = Energie_import
        fields = "__all__"

class Energie_exportSerializer(serializers.ModelSerializer):
    vestigingnaam = serializers.ReadOnlyField(source="vestiging.vestigingnaam")
    lattitude = serializers.ReadOnlyField(source="vestiging.lattitude")
    longitude = serializers.ReadOnlyField(source="vestiging.longitude")

    class Meta:
        model = Energie_export
        fields = "__all__"

class EnergieImportVestigingSerializer(serializers.ModelSerializer):
    vestigingnaam = serializers.ReadOnlyField(source="vestiging.vestigingnaam")
    vestiging_lattitude = serializers.ReadOnlyField(source="vestiging.lattitude")
    vestiging_longitude = serializers.ReadOnlyField(source="vestiging.longitude")
    belangenvereniging = serializers.ReadOnlyField(source="vestiging.bedrijf.belangenvereniging")
    sector = serializers.ReadOnlyField(source="vestiging.bedrijf.sector")
    
    class Meta:
        model = Energie_import
        fields = '__all__'

class Project_kerngetallenSerializer(serializers.ModelSerializer):
    vestiging = serializers.ReadOnlyField(source="project.vestiging.vestigingnaam")
    naam = serializers.ReadOnlyField(source="project.naam")
    omschrijving = serializers.ReadOnlyField(source="project.omschrijving")
    randvoorwaarden = serializers.ReadOnlyField(source="project.randvoorwaarden")
    afhankelijkheid_doorgaan = serializers.ReadOnlyField(source="project.afhankelijkheid_doorgaan")
    benodigde_innovatie = serializers.ReadOnlyField(source="project.benodigde_innovatie")
    mogelijke_versnelling = serializers.ReadOnlyField(source="project.mogelijke_versnelling")
    aanspraak_subsidie = serializers.ReadOnlyField(source="project.aanspraak_subsidie")

    
    class Meta:
        model = Project_kerngetallen
        fields = '__all__'

    
class ProjectSerializer(serializers.ModelSerializer):
    project_kerngetallen = Project_kerngetallenSerializer()
    vestigingnaam = serializers.ReadOnlyField(source="vestiging.vestigingnaam")

    

    class Meta:
        model = Project
        fields = '__all__'