from django.contrib import admin
from .models import User
from products.admin import BasketAdmin

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'instagram', 'phone')
    inlines = (BasketAdmin,)
admin.site.register(User, UserAdmin)