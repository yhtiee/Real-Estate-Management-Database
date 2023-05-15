from django.contrib import admin
from .models import *
# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ["vendor_name", "service", "email", "phone_number"]

admin.site.register(Vendor, VendorAdmin)