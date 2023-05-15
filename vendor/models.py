from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=256, null=False)
    service = models.CharField(max_length=256, null=False)
    email = models.CharField(max_length=256, null=False)
    phone_number = models.CharField(max_length=256, null=False)

    def __str__(self) -> str:
        return self.vendor_name