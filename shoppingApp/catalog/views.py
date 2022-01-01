from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
 
from catalog.models import Product
from catalog.serializer import ProductSerializer
 
class ProductAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Product.objects.all()
        serializer = ProductSerializer(categories, many=True)
        return Response(serializer.data)

def index(request):
    return HttpResponse("<h1>Product list</h1>")

def productsList(request):
    return HttpResponse("<h1>Product list</h1>")