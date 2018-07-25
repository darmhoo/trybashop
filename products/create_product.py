from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, ProductCategory
from .handle_uploaded import handle

from django import forms


class FormInscription(forms.Form):
    name = forms.CharField(label='Product Name', max_length=30)
    description = forms.CharField(label='Description', max_length=1000)
    price = forms.FloatField(label='price')
    status = forms.BooleanField(label='status')
    picture = forms.FileField()
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), label='Category' )


def page(request):
    if request.POST:
        form = FormInscription(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            status = form.cleaned_data['status']
            picture =  handle(request.FILES['file'])

            new_product = Product(name=name, description=description, category=category, price=price, status=status, image=picture )
            new_product.save()
            return HttpResponse("Product Added")
        else:
            return render(request, 'products/create_product.html', {'form': form})
    else:
        form = FormInscription()
        return render(request, 'products/create_product.html', {'form': form})
