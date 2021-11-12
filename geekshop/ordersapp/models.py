from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from baskets.models import Basket
from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен в обработку'),
        (PAID, 'оплачен'),
        (PROCEEDED, 'обрабатывается'),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменен'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    status = models.CharField(verbose_name='статус',
                              max_length=3,
                              choices=ORDER_STATUS_CHOICES,
                              default=FORMING)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'

    def __str__(self):
        return f'Текущий заказ: {self.id}'

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))


    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity * x.get_product_cost(), items)))

    def get_summary(self):
        items = self.orderitems.select_related()
        return {
            'total_cost': sum(list(map(lambda x: x.quantity * x.product.price, \
                                       items))),
            'total_quantity': sum(list(map(lambda x: x.quantity, items)))
        }

    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.save()

        self.is_active = False
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name="orderitems",
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                verbose_name='продукт',
                                on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество',
                                           default=0)

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.get(id=pk).quantity

    def get_product_cost(self):
        return self.product.price * self.quantity

@receiver(pre_save, sender=OrderItem)
@receiver(pre_save, sender=Basket)
def product_quantity_update_save(sender, instance, **kwargs):
    instance.product.quantity -= instance.quantity
    instance.product.save()

@receiver(pre_delete, sender=OrderItem)
@receiver(pre_delete, sender=Basket)
def product_quantity_update_delete(sender, instance, **kwargs):
    if instance.pk:
        instance.product.quantity -= instance.quantity - \
                                 instance.__class__.get_item(instance.pk)
        # instance.__class__.objects.get_item(id=instance.pk).quantity
    else:
        instance.product.quantity -= instance.quantity
    # if instance.product.quantity >= 0:
    instance.product.save()