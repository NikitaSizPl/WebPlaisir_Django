import datetime

from django.db import models
from user.models import User
from products.models import Product
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Покупатель',
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата создания',
    )
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    @property
    def total_price(self):
        total_price = sum(
            order_item.total_price for order_item in self.items.all())
        return total_price

    def __str__(self):
        return f"Заказ номер {self.id} для {self.user}"



class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Заказ'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    @property
    def total_price(self):
        if self.product.price is not None:
            total_price = self.product.price * self.quantity
        else:
            total_price = 0
        return total_price

    def __str__(self):
        return f'{self.total_price} в заказе {self.order.id}'


class OrderInfoForm(models.Model):
    user = models.CharField(
        max_length=50,
        verbose_name='Получатель'
    )
    instagram = models.CharField(
        max_length=30,
        verbose_name='Instagram',
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Phone',
        null=True,
        blank=True
    )
    delivery_date = models.CharField(
        verbose_name="Дата доставки/выдачи",
        max_length=15
    )
    add_info = models.CharField(
        max_length=255,
        verbose_name='Комментарий к заказу',
        null=True,
        blank=True
    )
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='order_info_form'
    )

    class Meta:
        verbose_name = 'Форма заказа'
        verbose_name_plural = 'Формы заказов'

    def __str__(self):
        return f"Заказ для {self.user} ({self.phone}) {self.instagram}"