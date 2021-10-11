from django.contrib import auth, messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from baskets.models import Basket
from geekshop.mixin import BaseClassContextMixin
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from users.models import User
from django.views.generic import ListView


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))


    else:
        form = UserLoginForm()
    content = {'title': 'Авторизация', 'col_lg': 'col-lg-5', 'action': 'Авторизация',
               'message': 'Нужен аккаунт? Зарегистрируйся',
               'form': form,
               }
    return render(request, 'users/login.html', content)

class UserLoginView(LoginView, BaseClassContextMixin):
    template_name = 'users/login.html'
    model = User
    # fields = ('login', 'password')
    form_class = UserLoginForm
    title = 'Авторизация'
    message = 'Нужен аккаунт? Зарегистрируйся',
    # success_url = reverse_lazy('/')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        return super(UserLoginView, self).get_context_data(**kwargs)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно прошли регистрацию")
            return HttpResponseRedirect(reverse('users:login'))

    else:
        form = UserRegisterForm()
    content = {'title': 'Регистрация', 'col_lg': 'col-lg-7', 'action': 'Регистрация',
               'message': 'Уже есть аккаунт? Авторизоваться',
               'form': form,
               }
    return render(request, 'users/register.html', content)

# @login_required
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)

    else:
        form = UserProfileForm(instance=request.user)
    content = {
        'title': 'GeekShop - Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'users/profile.html', content)

class Logout(LogoutView):
    template_name = 'mainapp/index.html'