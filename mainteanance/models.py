from django.db import models
from vendor.models import *
from property.models import *
# Create your models here.

class Mainteanance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="vendor_mainteanance")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="property_mainteanance")
    mainteanance = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=256, null=False)
    status = models.CharField(max_length=256, null=False)