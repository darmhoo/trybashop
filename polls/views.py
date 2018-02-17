from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Users


# Create your views here.
def index(request):
    context = {
        'list_of_users': Users.objects.order_by('id')
    }
    return render(request, 'base.html', context)
