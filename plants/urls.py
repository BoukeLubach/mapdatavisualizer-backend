from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apiviews import (
    VestigingViewSet, 
    EnergieImportViewSet, 
    EnergieExportViewSet, 
    EnergieVestigingImportListView, 
    ProjectViewSet, 
    ProjectkerngetallenViewSet,
    FilteredEnergieimportList,
    FilteredEnergieexportList
)

app_name = 'plants'
router = DefaultRouter()

router.register('api/vestiging', VestigingViewSet, basename='vestiging')
router.register('api/energieimport', EnergieImportViewSet, basename='energieimport')
router.register('api/energieexport', EnergieExportViewSet, basename='energieexport')
router.register('api/project', ProjectViewSet, basename='projecten')
router.register('api/projectkerngetallen', ProjectkerngetallenViewSet, basename='projectkerngetallen')

urlpatterns = [
    path('api/energieimportvestiging/', EnergieVestigingImportListView.as_view(), name="VestigingEnergieImportList"),
    path('api/FilteredEnergieimportList/<int:vestigingID>/', FilteredEnergieimportList.as_view(), name="FilteredEnergieimportList"),
    path('api/FilteredEnergieexportList/<int:vestigingID>/', FilteredEnergieexportList.as_view(), name="FilteredEnergieexportList"),
]

urlpatterns += router.urls
