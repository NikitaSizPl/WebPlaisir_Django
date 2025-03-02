from django.contrib import admin
from .models import Order, OrderItem, OrderInfoForm
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderInfoForm


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)

