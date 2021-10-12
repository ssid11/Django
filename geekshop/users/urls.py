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

from .views import login, register, profile, UserLoginView, Logout, UserRegisterView, UserProfileView

app_name = 'users'
urlpatterns = [
    # path('login/', login, name='login'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('register/', register, name='register'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    # path('profile/', UserProfileView.as_view(), name='profile'),
    # path('logout/', logout, name='logout'),
    path('logout/', Logout.as_view(), name='logout'),
]
