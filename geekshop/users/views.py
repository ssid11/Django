from django.contrib import auth, messages
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from baskets.models import Basket
from geekshop.mixin import BaseClassContextMixin
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserProfileEditForm
from users.models import User
from django.views.generic import ListView, FormView, UpdateView
from django.conf import settings



# Create your views here.

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#
#
#     else:
#         form = UserLoginForm()
#     content = {'title': 'Авторизация', 'col_lg': 'col-lg-5', 'action': 'Авторизация',
#                'message': 'Нужен аккаунт? Зарегистрируйся',
#                'form': form,
#                }
#     return render(request, 'users/login.html', content)

class UserLoginView(LoginView, BaseClassContextMixin):
    template_name = 'users/login.html'
    model = User
    form_class = UserLoginForm
    title = 'Авторизация'


class UserRegisterView(FormView,BaseClassContextMixin):
    title = 'Регистрация'
    template_name = 'users/register.html'
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_link(user):
                messages.success(request,'Вы успешно зарегистрировались. Проверьте почту.')
            return redirect(self.success_url)

        messages.error(request, str(form.errors))
        return redirect(self.success_url)


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Вы успешно прошли регистрацию")
#             return HttpResponseRedirect(reverse('users:login'))
#
#     else:
#         form = UserRegisterForm()
#     content = {'title': 'Регистрация', 'col_lg': 'col-lg-7', 'action': 'Регистрация',
#                'message': 'Уже есть аккаунт? Авторизоваться',
#                'form': form,
#                }
#     return render(request, 'users/register.html', content)

# @login_required
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#
#     else:
#         form = UserProfileForm(instance=request.user)
#     content = {
#         'title': 'GeekShop - Профиль',
#         'form': form,
#         'baskets': Basket.objects.filter(user=request.user),
#     }
#     return render(request, 'users/profile.html', content)

class Logout(LogoutView):
    template_name = 'mainapp/index.html'

class UserProfileView(UpdateView):
    title = 'Регистрация'
    template_name = 'users/profile.html'
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        context['profile'] = UserProfileEditForm(instance=self.request.user.userprofile)
        return context

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.pk)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST,files=request.FILES,instance=self.get_object())
        userprofile = UserProfileEditForm(data=request.POST, instance=request.user.userprofile)
        if form.is_valid() and userprofile.is_valid():
            form.save()
            # messages.success(request, "Вы успешно прошли регистрацию")
            return redirect(self.success_url)
        return redirect(self.success_url)

def send_verify_link(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])
    subject = f'Активация пользователя {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на портале GeekShop \n' \
              f' пройдите по ссылке {settings.DOMAIN_NAME}{verify_link}'
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email = email)
        if user and user.activation_key == activation_key and not user.is_activation_key_expired():
            user.activation_key_created=None
            user.activation_key=''
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return render(request,'users/verification.html')
    except Exception as e:
        HttpResponseRedirect(reverse('index'))

