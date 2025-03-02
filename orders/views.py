from django.shortcuts import render,redirect

from app import settings
from basket.models import Basket
from django.shortcuts import get_object_or_404
from .forms import OrdersForm
from .models import Order, OrderItem, OrderInfoForm
from django.contrib import messages

# Create your views here.

def create(request):
    form = OrdersForm()

    if request.user.is_authenticated:
        basket = get_object_or_404( Basket, user=request.user )
    else:
        basket_id = request.session.get( settings.BASKET_SESSION_ID )
        basket = Basket.objects.filter(id=basket_id).last()

    if request.method == 'POST':
        form = OrdersForm( data=request.POST )
        if form.is_valid():

            if request.user.is_authenticated:
                order = Order.objects.create(user=request.user)
            else:
                order = Order.objects.create()

            OrderInfoForm.objects.create(
                user = form.cleaned_data['user'],
                instagram = form.cleaned_data['instagram'],
                phone = form.cleaned_data['phone'],
                delivery_date = form.cleaned_data['delivery_date'],
                add_info = form.cleaned_data['add_info'],
                order=order
            )

            for item_basket in basket.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item_basket.product,
                    quantity=item_basket.quantity,
                    price=item_basket.total_price
                )
            basket.clear()
            return redirect('orders:thankyou', order.id)

        else:
            messages.error(request, 'Форма не была корректно обработана, введите данные еще раз')
            return redirect('orders:create')

    context = {
        'form': form,
        'basket': basket
    }
    return render(request, 'create.html', context)


def thankyou(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'thankyou.html', context)
