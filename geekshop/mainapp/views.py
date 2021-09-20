from django.shortcuts import render

import json
from .models import Product

# Create your views here.
def index(request):
    content = {'title':'geekshop start page'}
    return render(request,'mainapp/index.html',content)

def products(request):
    products = Product.objects.all()
    return render(request,'mainapp/products.html',{'products':products})
