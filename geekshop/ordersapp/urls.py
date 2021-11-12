from django.urls import path
from django.views.decorators.cache import cache_page
from .views import OrderCreate, OrderUpdate, OrderList, OrderDelete, OrderDetail, order_forming_complete, payment_result

app_name = 'ordersapp'
urlpatterns = [
    path('', cache_page(3600)(OrderList.as_view()), name='list'),
    path('create', cache_page(3600)(OrderCreate.as_view()), name='create'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='delete'),
    path('read/<int:pk>/', cache_page(3600)(OrderDetail.as_view()), name='read'),
    path('forming_complete/<int:pk>/', order_forming_complete, name='forming_complete'),
    path('payment/result/', payment_result, name='payment_result')
]