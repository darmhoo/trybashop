from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Category name', max_length=25)
    description = models.TextField(verbose_name='Describe the product category', max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "product Categories"


class Product(models.Model):
    name = models.CharField(verbose_name='Product name', max_length=25)
    description = models.TextField(verbose_name='Product description', max_length=1000)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Category')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    price = models.FloatField(verbose_name='product price', help_text='You should fix the price here');
    status = models.BooleanField()
    image = models.FileField(verbose_name='product image', upload_to='img/%Y/%m/%d/', default='./static/img/dami2.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})




