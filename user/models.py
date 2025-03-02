from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    name = models.CharField(
        max_length=50,
        verbose_name='Имя покупателя'
    )
    instagram = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        verbose_name='Instagram покупателя'
    )
    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name='Номер покупателя'
        )
    creat_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
        )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'