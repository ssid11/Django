from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from baskets.models import Basket
from mainapp.models import Product


# Create your views here.

@login_required
def basket_add(request, product_id):
    user_from_request = request.user
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=user_from_request, product=product)
    if not baskets.exists():
        Basket.objects.create(user=user_from_request, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, product_id):
    Basket.objects.get(id=product_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        result = render_to_string('baskets/baskets.html',{'baskets': baskets})
        return JsonResponse({'result': result})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))