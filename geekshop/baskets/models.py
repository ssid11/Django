from django.db import models

from mainapp.models import Product
from users.models import User


# Create your models here.
class BasketQSetManager(models.QuerySet):
    def delete(self, *args, **kwargs):
        for el in self:
            el.product.quantity += el.quantity
            el.product.save()
        super(BasketQSetManager, self).delete(*args, **kwargs)


class Basket(models.Model):
    # objects = BasketQSetManager.as_manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(id=pk).quantity

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk).quantity

    def delete(self, using=None, keep_parents=False):
        self.product.quantity += self.quantity
        self.save()
        super(Basket, self).delete()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk:
            self.product.quantity -= self.quantity - \
                                     self.__class__.get_item(self.pk).quantity
                            # self.__class__.objects.get_item(id=self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        # if self.product.quantity >= 0:
        self.product.save()
        super(Basket, self).save()
