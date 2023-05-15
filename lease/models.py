from django.db import models
from property.models import *
from tenant.models import *
# Create your models here.

class Lease(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="property_lease")
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="tenant_lease")
    lease = models.CharField(max_length=256, null=False)
    lease_start_date = models.DateField(max_length=256, null=False)
    lease_end_date = models.DateField(max_length=256, null=False)
    lease_amount = models.DecimalField(max_digits=256, decimal_places=2, null=False)

    def __str__(self) -> str:
        return self.lease