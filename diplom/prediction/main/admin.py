from django.contrib import admin

from .models import *

from import_export.admin import ImportExportActionModelAdmin
class ProductAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(features, ProductAdmin)
