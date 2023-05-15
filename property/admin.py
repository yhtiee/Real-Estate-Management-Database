from django.contrib import admin
from .models import *
# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ["property_name", "address", "size", "user", "expense", "tenant"]

    def user(self, obj):
        return obj.users.username
    
    def expense(self, obj):
        return obj.expenses.expense
    
    def tenant(self, obj):
        return obj.tenant.tenant_name
    
admin.site.register(Property, PropertyAdmin)