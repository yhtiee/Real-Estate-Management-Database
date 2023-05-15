from django.contrib import admin
from .models import *
# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display =["expense", "cost", "description" ]

admin.site.register(Expenses, ExpenseAdmin)