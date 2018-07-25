from django.urls import path
from . import views, create_product


urlpatterns = [
    path('', views.home, name='home'),
    path('create', create_product.page, name='create'),
]
