from django.shortcuts import render
from . import models


# Create your views here.


def home(request):
    items = models.Product.objects.all()
    return render(request, 'products/home.html', {'products': items})







