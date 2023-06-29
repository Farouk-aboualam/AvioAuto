from django.db import models
from home.models import Supplier


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.invoice_number
