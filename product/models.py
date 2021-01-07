from django.db import models
from django.utils import timezone

# Create your models here.

class Brand(models.Model):
    name = models.CharField(unique=True, max_length=30, blank=False,null=True)
    def __str__(self):
        return self.name


class Product(models.Model):

    genderChoice = (('W','Female'),('M','Male'),('U','Unisex'))

    id = models.BigIntegerField(primary_key=True, null=False)
    brand_name = models.ForeignKey(Brand, to_field='name', on_delete=models.CASCADE, related_name='brand_name', default='Brand Name') 
    name = models.CharField(max_length=300, blank=False,null=False)
    sex = models.CharField(max_length=7,choices=genderChoice, default='U')
    p_type = models.CharField(max_length=50, blank=True,null=True)
    image_link = models.CharField(max_length=500, blank=True,null=True)
    stock_price = models.DecimalField(max_digits=10,decimal_places=2, default=999.00)
    
    show = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    volume= models.CharField(max_length=50, blank=True,null=True)
    score = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=100, default=999.00, decimal_places=2)
    def __str__(self):
        
        template = '{0.name} {0.brand_name} {0.volume}  {0.price}'
        return template.format(self)
    
    

"""
class Pricing(models.Model):
    product =models.ForeignKey(Product, on_delete=models.CASCADE,related_name='prices',null=True)
    
    
     
    price= models.DecimalField(max_digits=8,decimal_places=2, default=9999, null=True)
    volume= models.IntegerField(null=True)
    def __str__(self):
         return self.product.name,self.price, self.volume

"""


    



    