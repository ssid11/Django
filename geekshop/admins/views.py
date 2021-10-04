from users.models import User
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

def index(request):
    return render(request,'admins/admin.html', {'title':'административная панель'})

class UserListView(ListView):
    model = User
    template_name = 'admins/admin-user-read.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админпанель | Пользователи'
        return context

class UserCreateView(CreateView):
    pass

class UserUpdateView(UpdateView):
    pass

class UserDeleteView(DeleteView):
    pass
