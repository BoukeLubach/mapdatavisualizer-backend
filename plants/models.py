from django.db import models

class Bedrijf(models.Model):
    naam = models.CharField(max_length=124, unique=True)
    holding = models.CharField(max_length=124, null=True, blank=True)
    sector = models.CharField(max_length=124, null=True, blank=True)
    belangenvereniging = models.CharField(max_length=124, null=True, blank=True)
    
    def __str__(self):
        return self.naam


class Vestiging(models.Model):
    vestigingnaam = models.CharField(max_length=124)
    bedrijf = models.ForeignKey(Bedrijf, on_delete=models.CASCADE, related_name="vestiging_naam")
    lattitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    adres = models.CharField(max_length=124, blank=True, null=True)
    postcode = models.CharField(max_length=124, blank=True, null=True)
    woonplaats = models.CharField(max_length=124, blank=True, null=True)
    productiegroei_2020_2025 = models.FloatField(default=0, blank=True, null=True)
    productiegroei_2020_2030 = models.FloatField(default=0, blank=True, null=True)
    wkk = models.BooleanField(default=False)
    wkk_2030 = models.BooleanField(default=False)

    class Meta:
        unique_together = ['vestigingnaam', 'lattitude', 'longitude']

    def __str__(self):
        return self.vestigingnaam

class Project(models.Model):
    vestiging = models.ForeignKey(Vestiging, related_name="vestiging_project", on_delete=models.CASCADE)
    naam = models.CharField(max_length=124)
    omschrijving = models.CharField(max_length=124, blank=True, null=True)
    randvoorwaarden = models.CharField(max_length=124, blank=True, null=True)
    afhankelijkheid_doorgaan = models.CharField(max_length=124, blank=True, null=True)
    benodigde_innovatie = models.CharField(max_length=124, blank=True, null=True)
    mogelijke_versnelling = models.CharField(max_length=124, blank=True, null=True)
    aanspraak_subsidie = models.CharField(max_length=124, blank=True, null=True)
    
    class Meta:
        unique_together = ['vestiging', 'naam']

    def __str__(self):
        return self.naam

class Project_kerngetallen(models.Model):
    ZEKER = "zeker"
    VOORW = "voorw"
    ONZEKER = "onzeker"

    STATUS_OPTIONS = (
        (ZEKER, "Zeker"),
        (VOORW, "Voorwaardelijk"),
        (ONZEKER, "Onzeker"),
    )
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    aardgas_verandering = models.FloatField(default=0)
    biogas_verandering = models.FloatField(default=0)
    elektriciteit_verandering  = models.FloatField(default=0)
    verzwaring_netaansluiting = models.FloatField(default=0)
    stoom_verandering  = models.FloatField(default=0)
    overige_warmte_verandering = models.FloatField(default=0)
    biomassa_verandering = models.FloatField(default=0)
    afval_verandering = models.FloatField(default=0)
    waterstof_energie_verandering = models.FloatField(default=0)
    productie_verandering = models.FloatField(default=0)
    co2_uitstoot_verandering  = models.FloatField(default=0)
    nox_uitstoot_verandering  = models.FloatField(default=0)
    jaar_realisatie = models.IntegerField()
    status = models.CharField(max_length=8, choices=STATUS_OPTIONS, default=ONZEKER)




class Energie_import(models.Model):
    vestiging = models.ForeignKey(Vestiging, related_name='vestiging_energieimport', on_delete=models.CASCADE)
    jaar = models.IntegerField()
    aardgas = models.FloatField(default=0)
    biogas = models.FloatField(default=0)
    elektriciteit = models.FloatField(default=0)
    stoom = models.FloatField(default=0)
    overige_warmte = models.FloatField(default=0)
    biomassa = models.FloatField(default=0)
    afval = models.FloatField(default=0)
    waterstof = models.FloatField(default=0)
    co2 = models.FloatField(default=0)
    
    class Meta:
        unique_together = ['vestiging', 'jaar']

class Energie_export(models.Model):
    vestiging = models.ForeignKey(Vestiging, related_name='vestiging_energieexport', on_delete=models.CASCADE)
    jaar = models.IntegerField()
    aardgas = models.FloatField(default=0)
    biogas = models.FloatField(default=0)
    elektriciteit = models.FloatField(default=0)
    stoom = models.FloatField(default=0)
    overige_warmte = models.FloatField(default=0)
    biomassa = models.FloatField(default=0)
    afval = models.FloatField(default=0)
    waterstof = models.FloatField(default=0)
    co2 = models.FloatField(default=0)

    class Meta:
        unique_together = ['vestiging', 'jaar']
