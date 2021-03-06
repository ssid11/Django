from django.urls import reverse_lazy,reverse

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductForm
from mainapp.models import Product, ProductCategory
from users.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from  django.http import HttpResponseRedirect
from geekshop.mixin import CustomDispatchMixin
from .forms import CategoryCreateForm
# Create your views here.

def index(request):
    return render(request,'admins/admin.html', {'title':'административная панель'})

class UserListView(ListView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Пользователи'
        return context

class UserCreateView(CreateView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admins_user')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Регистрация'
        return context

class UserUpdateView(UpdateView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admins_user')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Редактирование пользователя'
        return context

class UserDeleteView(DeleteView, CustomDispatchMixin):

    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admins_user')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ProductListView(ListView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Номенклатура'
        return context

class ProductUpdateView(UpdateView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductForm
    # form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admins_product')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Редактирование номенклатуры'
        return context

    def get(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).post(request, *args, **kwargs)

class ProductDeleteView(DeleteView):

    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admins_product')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        # self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ProductCreateView(CreateView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductForm
    success_url = reverse_lazy('admins:admins_product')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Создание номенклатуры'
        return context

    # def post(self, request, *args, **kwargs):
    #     return super(ProductCreateView, self).post(request, *args, **kwargs)
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(data=request.POST)
    #     # instance = self.get_object()
    #     if form.is_valid():
    #         form.save()
    #         return redirect(self.success_url)
    #     return redirect(self.success_url)

class CategoryListView(ListView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Категории'
        return context

class CategoryUpdateView(UpdateView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = CategoryCreateForm
    success_url = reverse_lazy('admins:admins_category')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Редактирование категории'
        return context

class CategoryCreateView(CreateView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    form_class = CategoryCreateForm
    success_url = reverse_lazy('admins:admins_сcategory')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Создание категории'
        return context

class CategoryDeleteView(DeleteView):

    model = ProductCategory
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admins_category')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        # self.object.save()
        return HttpResponseRedirect(self.get_success_url())