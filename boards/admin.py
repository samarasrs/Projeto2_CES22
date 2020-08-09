from django.contrib import admin
from import_export import resources
from .models import BrazilData, SaoPauloData, SudesteData, EstadosData, RegiaoData
from import_export.admin import ImportExportModelAdmin


class BrazilDataResource(resources.ModelResource):
    class Meta:
        model = BrazilData
        widgets = {
            'date': {'format': '%d/%m/%Y'},
        }


class BrazilDataAdmin(ImportExportModelAdmin):
    resource_class = BrazilDataResource


admin.site.register(BrazilData, BrazilDataAdmin)


class SudesteDataResource(resources.ModelResource):
    class Meta:
        model = SudesteData
        widgets = {
            'date': {'format': '%d/%m/%Y'},
        }


class SudesteDataAdmin(ImportExportModelAdmin):
    resource_class = SudesteDataResource


admin.site.register(SudesteData, SudesteDataAdmin)


class SaoPauloDataResource(resources.ModelResource):
    class Meta:
        model = SaoPauloData
        widgets = {
            'date': {'format': '%d/%m/%Y'},
        }


class SaoPauloDataAdmin(ImportExportModelAdmin):
    resource_class = SaoPauloDataResource


admin.site.register(SaoPauloData, SaoPauloDataAdmin)


class EstadosDataResource(resources.ModelResource):
    class Meta:
        model = EstadosData


class EstadosDataAdmin(ImportExportModelAdmin):
    resource_class = EstadosDataResource


admin.site.register(EstadosData, EstadosDataAdmin)


class RegiaoDataResource(resources.ModelResource):
    class Meta:
        model = RegiaoData


class RegiaoDataAdmin(ImportExportModelAdmin):
    resource_class = RegiaoDataResource


admin.site.register(RegiaoData, RegiaoDataAdmin)

# Register your models here.
