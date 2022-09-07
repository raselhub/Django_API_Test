
from rest_framework import serializers 
from .models import Products
class ProductsSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model =  Products
        fields = ('name', 'quantity', 'price', 'promo', 'bsale', 'aka', 'date')