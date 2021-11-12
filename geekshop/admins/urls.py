"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import index, UserDeleteView, UserListView, UserUpdateView, UserCreateView, ProductListView, \
    ProductUpdateView, CategoryListView, CategoryUpdateView, CategoryCreateView, CategoryDeleteView, ProductDeleteView, \
    ProductCreateView

app_name = 'admins'
urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admins_user'),
    path('users-create/', UserCreateView.as_view(), name='admins_user_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(), name='admins_user_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admins_user_delete'),
    path('products/', ProductListView.as_view(), name='admins_product'),
    path('products-create/', ProductCreateView.as_view(), name='admins_product_create'),
    path('products-update/<int:pk>', ProductUpdateView.as_view(), name='admins_product_update'),
    path('products-delete/<int:pk>', ProductDeleteView.as_view(), name='admins_product_delete'),
    path('categories/', CategoryListView.as_view(), name='admins_category'),
    path('categories-update/<int:pk>', CategoryUpdateView.as_view(), name='admins_category_update'),
    path('categories-create/', CategoryCreateView.as_view(), name='admins_category_create'),
    path('categories-delete/<int:pk>', CategoryDeleteView.as_view(), name='admins_category_delete'),
]
