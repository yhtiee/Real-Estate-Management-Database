from django.contrib import admin
from .models import *
# Register your models here.

class MainteananceAdmin(admin.ModelAdmin):
    list_display = ["mainteanance", "description", "status", "property" ]

    # def vendor(self, obj):
    #     return obj.vendors.vendor_name
    
    def property(self, obj):
        return obj.propertys.property_name

admin.site.register(Mainteanance, MainteananceAdmin)