from django.db import models
from product.models import Product 
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=80, blank=False)
    email = models.CharField(max_length=80, blank=True)
    phone = models.CharField(max_length=80, blank=False)
    city = models.CharField(max_length=80, blank=True)
    handeld = models.BooleanField(default=False)
    deliverd = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.name} {0.phone} {0.email} {0.city}'
        return template.format(self)
  


class ProductList(models.Model):

    products = models.ForeignKey(Product, on_delete=models.CASCADE) 
    orderBy = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    
    quantity = models.IntegerField()
    
    def __str__(self):
        template = '{0.products.name} {0.quantity} {0.orderBy.name}'
        return template.format(self)
