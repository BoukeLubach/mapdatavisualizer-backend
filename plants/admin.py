from django.contrib import admin
from .models import Bedrijf, Energie_export, Energie_import, Project_kerngetallen, Vestiging, Project
# Register your models here.


admin.site.register(Bedrijf)
admin.site.register(Vestiging)
admin.site.register(Project)
admin.site.register(Project_kerngetallen)
admin.site.register(Energie_import)
admin.site.register(Energie_export)
