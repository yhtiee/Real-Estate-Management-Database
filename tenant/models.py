from django.db import models

# Create your models here.

class Tenant(models.Model):
    tenant_name = models.CharField(max_length=256, null=False)
    phone_number = models.CharField(max_length=256, null=False)
    email = models.CharField(max_length=256, null=False)

    def __str__(self) -> str:
        return self.tenant_name