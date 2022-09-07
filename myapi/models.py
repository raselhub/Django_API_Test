from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=80)
    quantity = models.IntegerField()
    bsale = models.IntegerField()
    aka = models.CharField(max_length=60)
    promo = models.CharField(max_length=60)
    price = models.IntegerField()
    # image = models.ImageField(upload_to='images/')
    date = models.DateField()

def __str__(Self):
    return Self.aka


