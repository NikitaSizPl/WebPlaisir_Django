from django.db import models
from user.models import User
from products.models import Product
from django.utils import timezone


# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='baskets',
        verbose_name='Покупатель',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания'
    )

    data_to = models.DateField(
        null=True,
        blank=True,
        verbose_name='На когда делается заказ'
    )

    def clear(self):
        self.items.all().delete()

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

    @property
    def total_quantity(self):
        return sum(item.total_quantity for item in self.items.all())

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"Корзина {self.id} для {self.user if self.user else 'Анонимного пользователя'}, Сумма заказа: {self.total_price},На когда: {self.data_to}"


class BasketItem(models.Model):
    basket = models.ForeignKey(
        Basket,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name='Корзина'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )

    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество'
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

    @property
    def total_quantity(self):
        if self.quantity is None:
            return 0
        return self.quantity

    def __str__(self):
        return f"Товар: {self.product.name}, Кол-во: {self.total_quantity}, Цена: {self.total_price}"