from django.shortcuts import render
import json

# Create your views here.
def index(request):
    content = {'title':'geekshop start page'}
    return render(request,'mainapp/index.html',content)

def products(request):
    PRODUCT_DIR = 'vendor/img/products/'
    with open('.\\mainapp\\fixtu\\db.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
    return render(request,'mainapp/products.html',content)
