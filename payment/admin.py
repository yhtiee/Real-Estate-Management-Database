from django.contrib import admin
from .models import *
# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ["payment", "amount", "payment_date", "lease", "tenant"]

    def tenant(self, obj):
        return obj.tenant.tenant_name
    
    def lease(self, obj):
        return obj.lease.lease
    
admin.site.register(Payment, PaymentAdmin)