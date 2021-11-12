from baskets.models import Basket


def basket(request):
    basket_lst = []
    if request.user.is_authenticated:
        basket_lst = Basket.objects.select_related().filter(user=request.user)

    return {
            'baskets':basket_lst,
    }