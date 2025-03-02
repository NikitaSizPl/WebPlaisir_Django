from django.urls import path
from .views import create, thankyou

app_name = 'orders'

urlpatterns = [
    path('create/', create, name='create'),
    path('thankyou/<int:order_id>/', thankyou, name='thankyou'),
]
