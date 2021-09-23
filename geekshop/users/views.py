from django.shortcuts import render


# Create your views here.
def login(request):
    content = {'title':'Авторизация', 'col_lg':'col-lg-5', 'href':'register.html', 'action':'Авторизация',
               'message':'Нужен аккаунт? Зарегистрируйся',
    }
    return render(request,'users/login.html', content)


def register(request):
    content = {'title': 'Регистрация', 'col_lg': 'col-lg-7','href':'login.html', 'action': 'Регистрация',
               'message': 'Уже есть аккаунт? Авторизоваться',
               }
    return render(request,'users/login.html', content)
