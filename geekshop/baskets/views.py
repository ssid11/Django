from django.shortcuts import render, HttpResponseRedirect
from mainapp.models import Product
from users.models import User
from baskets.models import Basket

# Create your views here.
def basket_add(request, product_id):
    user_from_request = request.user
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=user_from_request, product=product)
    if not baskets.exists():
        Basket.objects.create(user=user_from_request, product=product, quantity = 1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_remove(request, product_id):
    Basket.objects.get(id=product_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

