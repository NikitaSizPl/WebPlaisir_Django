from django.db import models


# Модель категории
class Catigories(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
        )
    description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Описание',
        )
    image = models.ImageField(
        upload_to='images',
        null=True,
        blank=True,
        verbose_name='Изображение'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Модель товара
class Product(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        verbose_name='Название'
        )
    description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Описание',
        )
    price = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Цена'
        )
    image = models.ImageField(
        upload_to='images',
        null=True,
        blank=True,
        verbose_name='Изображение'
        )
    # Зависимость к классу Catigories
    categories = models.ForeignKey(
        Catigories,
        on_delete=models.CASCADE,
        verbose_name='Категория'
        )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
