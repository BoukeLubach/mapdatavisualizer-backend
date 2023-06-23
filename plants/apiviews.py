
from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from .serializers import ( 
    VestigingSerializer, 
    Energie_importSerializer, 
    Energie_exportSerializer,
    EnergieImportVestigingSerializer,
    ProjectSerializer,
    Project_kerngetallenSerializer,
)

from .models import Vestiging, Energie_export, Energie_import, Project, Project_kerngetallen


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000




class VestigingViewSet(viewsets.ModelViewSet):
    serializer_class = VestigingSerializer
    queryset = Vestiging.objects.all()
    # pagination_class = LargeResultsSetPagination
    pagination_class = None

class EnergieImportViewSet(viewsets.ModelViewSet):
    serializer_class = Energie_importSerializer
    queryset = Energie_import.objects.all()
    pagination_class = None
    
class EnergieExportViewSet(viewsets.ModelViewSet):
    serializer_class = Energie_exportSerializer
    queryset = Energie_export.objects.all() 
    pagination_class = None




class EnergieVestigingImportListView(generics.ListAPIView):
    serializer_class = EnergieImportVestigingSerializer
    queryset = Vestiging.objects.all() 
    pagination_class = None

class ProjectViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    pagination_class = None

class ProjectkerngetallenViewSet(viewsets.ModelViewSet):
    
    serializer_class = Project_kerngetallenSerializer
    queryset = Project_kerngetallen.objects.all()
    pagination_class = None


class FilteredEnergieimportList(generics.ListAPIView):
    serializer_class = Energie_importSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        vestigingID = self.kwargs['vestigingID']
        return Energie_import.objects.filter(vestiging=vestigingID)

        
class FilteredEnergieexportList(generics.ListAPIView):
    serializer_class = Energie_exportSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        vestigingID = self.kwargs['vestigingID']
        return Energie_export.objects.filter(vestiging=vestigingID)
