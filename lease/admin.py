from django.contrib import admin
from .models import *
# Register your models here.

class LeaseAdmin(admin.ModelAdmin):
    list_display = ["lease", "lease_start_date", "lease_end_date", "lease_amount", "tenant", "property" ]

    def tenant(self, obj):
        return obj.tenant.tenant_name
    
    def property(self, obj):
        return obj.propertys.property_name

admin.site.register(Lease, LeaseAdmin)