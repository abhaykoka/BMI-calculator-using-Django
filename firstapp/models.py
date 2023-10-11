from django.db import models

# Create your models here.
from .models import *

class Customer(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.CharField(max_length=20,null=True)
    dateCreated=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor'),
        ('General','General')
    )
    name=models.CharField(max_length=100,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=100,null=True,choices=CATEGORY)
    tags=models.ManyToManyField(Tag)
    def __str__(self):
        return self.name
class Order(models.Model):
        STATUS=(
            ('Pending','Pending'),
            ('Out for delivery','Out for delivery'),
            ('Delivered','Delivery')
        )
        status=models.CharField(max_length=100,null=True,choices=STATUS)
        Customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
        Product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)    


