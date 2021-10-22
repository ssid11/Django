from django.urls import path
from .views import OrderCreate, OrderList, OrderDelete, order_forming_complete, OrderDetail, OrderUpdate

app_name = 'ordersapp'
urlpatterns = [
    path('', OrderList.as_view(), name='list'),
    path('create', OrderCreate.as_view(), name='create'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='delete'),
    path('read/<int:pk>/', OrderDetail.as_view(), name='read'),
    path('aa/<int:pk>/', OrderList.as_view(), name='forming_complete'),
]
