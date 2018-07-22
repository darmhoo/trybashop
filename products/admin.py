from django.contrib import admin
from .models import ProductCategory
from .models import Product

# Register your models here.



admin.site.register(ProductCategory)
admin.site.register(Product)
