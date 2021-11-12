from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Категория")
    description = models.TextField(max_length=512, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True, verbose_name="Товар")
    description = models.TextField(max_length=512, blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    ing = models.ImageField(upload_to='products_images', blank=True, verbose_name="Фото")

    def __str__(self):
        return f'{self.name} | {self.category}'

# Create your models here.
