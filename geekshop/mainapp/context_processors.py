from baskets.models import Basket


def basket(request):
    basket_lst = []
    if request.user.is_authenticated:
        basket_lst = Basket.objects.filter(user=request.user)

    return {
            'baskets':basket_lst,
    }