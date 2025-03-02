from django.contrib import admin
from .models import Basket, BasketItem

class BasketItemInline(admin.TabularInline):
    model = BasketItem

class BasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_price']
    inlines = [BasketItemInline]

# Register your models here.
admin.site.register(Basket, BasketAdmin)
