from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=64,unique=True)
    description = models.TextField(max_length=512,blank=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=512, blank=True)
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    quantity = models.PositiveIntegerField(default=0)
    ing = models.ImageField(upload_to='products_images', blank=True)

    def __str__(self):
        return f'{self.name}|{self.category}'

# Create your models here.
