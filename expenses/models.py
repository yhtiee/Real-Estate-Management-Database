from django.db import models

# Create your models here.

class Expenses(models.Model):
    expense = models.CharField(max_length=256, null=False)
    cost = models.DecimalField(max_digits=256, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=256, null=False)

    def __str__(self) -> str:
        return self.expense