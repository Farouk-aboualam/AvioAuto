from django.db import models
from home.models import Supplier, Product


class Order(models.Model):
    title = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    payment_method = models.CharField(max_length=10, choices=(
        ('value1', 'Par chèque'),
        ('value2', 'Par éspèces'),
        ('value3', 'Par virement'),
    ), default='value2')
    products = models.ManyToManyField(Product, through='OrderProduct')

    def __str__(self):
        return self.title


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
