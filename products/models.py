from django.db import models
from polls.models import UserProfile


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Category name', max_length=25)
    description = models.TextField(verbose_name='Describe the product category', max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(verbose_name='Product name', max_length=25)
    description = models.TextField(verbose_name='Product description', max_length=1000)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Category')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='creator')
    price = models.FloatField(verbose_name='product price', help_text='You should fix the price here');
    status = models.BooleanField()



