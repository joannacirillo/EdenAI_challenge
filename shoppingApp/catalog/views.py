from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(index.html)

def productsList(request):
    return HttpResponse("<h1>Product list</h1>")