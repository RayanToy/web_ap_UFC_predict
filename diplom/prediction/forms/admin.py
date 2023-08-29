from django.contrib import admin
from .models import UFC_data
from .models import *

from import_export.admin import ImportExportActionModelAdmin
class ProductAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(UFC_data, ProductAdmin)
# Register your models here.
