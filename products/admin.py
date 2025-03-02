from django.contrib import admin
from .models import Catigories, Product
from basket.models import Basket

# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image']
    list_editable = ['description', 'image']
    prepopulated_fields = {'name': ('name',)}
    ordering = ('id',)
admin.site.register(Catigories, CategoriesAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'image']
    list_editable = ['description', 'price', 'image']
    prepopulated_fields = {'name': ('name',)}
    ordering = ('id',)
admin.site.register(Product, ProductAdmin)

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = None