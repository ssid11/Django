from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.template.loader import render_to_string

from .models import Product, ProductCategory


# Create your views here.
def index(request):
    content = {'title': 'geekshop start page'}
    return render(request, 'mainapp/index.html', content)


def products(request, category_id=None, page_id=1):
    categories = ProductCategory.objects.all()
    products = Product.objects.filter(category_id=category_id) if category_id != None else Product.objects.all()
    paginator = Paginator(products,per_page=2)
    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context ={'categories': categories,}
    context.update({'products': products_paginator})

    return render(request, 'mainapp/products.html', context)

def cat_change(request, id):
    if request.is_ajax():
        products = Product.objects.filter(category=id)
        try:
            result = render_to_string('mainapp/produts_box.html',{'products': products})
        except Exception as e:
            print(e)
        return  JsonResponse({'result': result})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
