from django.contrib import admin
from .models import Supplier, Product
from .models import CustomUser

admin.site.register(CustomUser)
admin.site.register(Supplier)
admin.site.register(Product)
