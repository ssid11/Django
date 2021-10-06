from django.urls import reverse_lazy

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from users.models import User
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from  django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,'admins/admin.html', {'title':'административная панель'})

class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Пользователи'
        return context

class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admins_user')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Регистрация'
        return context

class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admins_user')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Редактирование пользователя'
        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admins_user')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
