from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, verbose_name="Фото")
    age =models.PositiveIntegerField(verbose_name="Возраст", default=18)
    activation_key = models.CharField(max_length=128, blank=True, verbose_name="Ключ активации")

    fields = ('login', 'password')
