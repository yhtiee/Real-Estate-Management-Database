from django.contrib import admin
from .models import *
# Register your models here.

class TenantAdmin(admin.ModelAdmin):
    list_display = ["tenant_name", "phone_number", "email"]

admin.site.register(Tenant, TenantAdmin)