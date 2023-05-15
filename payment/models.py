from django.db import models
from lease.models import *
from tenant.models import *
# Create your models here.

class Payment(models.Model):
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name="payment_lease")
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="tenant_payment")
    payment = models.CharField(max_length=256, null=False)
    amount = models.DecimalField(max_digits=256, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)

