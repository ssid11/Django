from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm


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


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Вы успешно прошли регистрацию")
            return HttpResponseRedirect(reverse('users:login'))

    else:
        form = UserRegisterForm()
    content = {'title': 'Регистрация', 'col_lg': 'col-lg-7', 'action': 'Регистрация',
               'message': 'Уже есть аккаунт? Авторизоваться',
               'form': form,
               }
    return render(request, 'users/register.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

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
    }
    return render(request,'users/profile.html', content)
