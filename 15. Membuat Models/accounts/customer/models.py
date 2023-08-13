from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    CATEGORY=(('Indoor','Indoor'),
		('Out Door','Out Door'),)
    name=models.CharField(max_length=200, null=True,choices=CATEGORY)
    description=models.CharField(max_length=200,null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

class Order(models.Model):
    #customer=
    #Product=
    
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True)