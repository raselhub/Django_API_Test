from django.shortcuts import render

# Create your views here.
# views.py 
from rest_framework import viewsets
from .serializers import ProductsSerializer 
from .models import Products
class ProductsViewSet(viewsets.ModelViewSet): 
    queryset = Products.objects.all().order_by('aka') 
    serializer_class = ProductsSerializer