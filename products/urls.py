from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [

    path("", index, name="index"),
    path("categories/", categories, name="categories"),
    path("categories/<str:cat_name>", items_categor, name="items_categor"),
    path('item/<int:product_id>', product_id, name='item_id'),
]
