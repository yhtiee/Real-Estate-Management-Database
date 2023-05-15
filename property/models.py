from django.db import models
from django.contrib.auth.models import User
from expenses.models import *
from tenant.models import *
# Create your models here.

class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_property")
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE, related_name="property_expense", null=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="tenant_property", null=True)
    property_name = models.CharField(max_length=256, null=False)
    address = models.CharField(max_length=256, null=False)
    size = models.CharField(max_length=256, null=False)
