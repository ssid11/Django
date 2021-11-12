from django.db import  connection
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.db.models import F, Q
from baskets.models import Basket
from mainapp.models import Product


# Create your views here.

@login_required
def basket_add(request, product_id):
    user_from_request = request.user
    product = Product.objects.select_related().get(id=product_id)
    baskets = Basket.objects.filter(user=user_from_request, product=product).select_related()
    if not baskets.exists():
        Basket.objects.create(user=user_from_request, product=product, quantity=1)
    else:
        basket = baskets.first()
        # basket.quantity += 1
        basket.quantity = F('quantity') + 1
        basket.save()
        up_qr = list(filter(lambda x: 'UPDATE' in x['sql'], connection.queries))
        print(f'Basket add query {up_qr}')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, product_id):
    Basket.objects.get(id=product_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.select_related().get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.select_related().filter(user=request.user)
        result = render_to_string('baskets/baskets.html',{'baskets': baskets})
        return JsonResponse({'result': result})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def add_ajax(request, product_id):
    user_from_request = request.user
    product = Product.objects.select_related().get(id=product_id)
    baskets = Basket.objects.select_related().filter(user=user_from_request, product=product)
    if not baskets.exists():
        Basket.objects.create(user=user_from_request, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    # try:
    #     result = render_to_string('mainapp/produts_box.html', {'products': products})
    # except Exception as e:
    #     print(e)
    return JsonResponse({'result': f"Товар {product.name} добавлен в корзину."})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
