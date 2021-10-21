from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, verbose_name="Фото")
    age =models.PositiveIntegerField(verbose_name="Возраст", default=18)
    activation_key = models.CharField(max_length=128, blank=True, null=True, verbose_name="Ключ активации")
    activation_key_created = models.DateTimeField(auto_now=True , blank=True, null=True)

    fields = ('login', 'password')
    def is_activation_key_expired(self):
        return True if self.activation_key_created + timedelta(hours=48) <= now() else False

class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(User, unique=True, null=False,db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    about = models.TextField(verbose_name='о себе', max_length=512, blank=True, null=True)
    gender = models.CharField(verbose_name='пол', max_length=5, choices=GENDER_CHOICES, blank=True)
