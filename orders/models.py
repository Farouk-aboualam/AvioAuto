from django.db import models
from home.models import Supplier


class Order(models.Model):
    title = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # Payment methode
    # 2d array of products, quantity
    # is_paid (default = false)

    def __str__(self):
        return self.title
