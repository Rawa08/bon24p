from django.urls import path
from .views import my_cart, add_product, adjust, delete_from_cart





urlpatterns = [
    path('', my_cart, name='my_cart'),
   
    path('add', add_product, name='add_product'),
    path('adjust/(<id>)', adjust, name='adjust'),
    path('delete/(<id>)', delete_from_cart, name='delete'),
   ]