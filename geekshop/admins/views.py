from django.urls import reverse_lazy

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from mainapp.models import Product, ProductCategory
from users.models import User
from django.shortcuts import render
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
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admins_user')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Редактирование пользователя'
        return context

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
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admins_user')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Редактирование пользователя'
        return context

# class CategoryCreateView(CreateView, CustomDispatchMixin):
#     model = ProductCategory
#     template_name = 'admins/admin-categories-create.html'
#     form_class = CategoryCreateForm
#     success_url = reverse_lazy('admins:admins_category')
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(CategoryCreateView, self).get_context_data(**kwargs)
#         context['title'] = 'Админпанель | Создание категории'
#         return context

def admins_category_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CategoryCreateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse_lazy('admins:admins_category'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CategoryCreateForm()

    return render(request,'admins/admin-categories-create.html', {'title':'административная панель | Создание категории', 'form': form})

def admins_category_update(request, pk):
    if request.method == 'POST':
        pass
    #     # create a form instance and populate it with data from the request:
    #     form = CategoryCreateForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         category = ProductCategory.objects.get(id=pk)
    #
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponseRedirect(reverse_lazy('admins:admins_category'))

    # if a GET (or any other method) we'll create a blank form
    else:
        category = ProductCategory.objects.get(id=pk)
        form = CategoryCreateForm(instance=category)

    return render(request,'admins/admin-categories-create.html', {'title':'административная панель', 'form': form})