import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from basket.models import Basket, BasketItem
from products.models import Product
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def basket_base(request):
    # если пользователь авторизован
    if request.user.is_authenticated:
        # получаем корзину авторизованого пользователя
        basket, create = Basket.objects.get_or_create(user=request.user)
    # если пользователь не авторизован
    else:
        # получаем корзину из сессии
        basket_id = request.session.get(settings.BASKET_SESSION_ID)
        if not basket_id:
            # создаем корзину для сессии
            basket = Basket.objects.create()
            request.session[settings.BASKET_SESSION_ID] = basket.id
        else:
            # получаем корзину если она создана
            basket = Basket.objects.filter(id=basket_id).first()
    context = {
        'basket': basket,
        'basket_item': BasketItem.objects.filter(basket=basket),
    }
    return render(request, 'basket/basket.html', context)


def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Для авторизованых пользователей
    if request.user.is_authenticated:
        basket, create = Basket.objects.get_or_create(user=request.user)
        basket_item = BasketItem.objects.filter(basket=basket, product=product).first()
    # Для анонимных пользователей
    else:
        # получаем корзину из сессии
        basket_id = request.session.get(settings.BASKET_SESSION_ID)
        if not basket_id:
            # создаем корзину для сессии
            basket = Basket.objects.create()
            request.session[settings.BASKET_SESSION_ID] = basket.id
        else:
            # получаем корзину если она создана
            basket = Basket.objects.get(id=basket_id)
        basket_item = BasketItem.objects.filter(basket=basket, product=product).first()

    if basket_item:
        basket_item.quantity += 1
        basket_item.save()
    else:
        BasketItem.objects.create(basket=basket, product=product, quantity=1)
    return redirect('basket:basket')


def del_from_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Для авторизованых пользователей
    if request.user.is_authenticated:
        basket = Basket.objects.get(user=request.user)
        basket_item = BasketItem.objects.filter(basket=basket, product=product).first()
    else:
        # Для анонимных пользователей
        basket = request.session.get('basket_id')
        basket_item = BasketItem.objects.filter(basket=basket, product=product).first()
    if basket_item:
        basket_item.delete()
    return redirect('basket:basket')


# @csrf_exempt
def update_basket(request):
    if request.method == "POST":
        try:
            data = json.loads( request.body )
            item_id = data.get("item_id")
            quantity = int( data.get("quantity"))

            print( f"📩 Пришли данные: item_id={item_id}, quantity={quantity}")

            basket_item = BasketItem.objects.get(id=item_id)
            basket_item.quantity = quantity
            basket_item.save()  # Здесь total_price пересчитается автоматически

            basket = Basket.objects.get( id=basket_item.basket.id )

            return JsonResponse( {
                "success": True,
                "item_total_price": basket_item.total_price,  # Теперь это @property
                "basket_total_price": sum( item.total_price for item in basket.items.all() )
            } )
        except BasketItem.DoesNotExist:
            return JsonResponse({"success": False, "message": "Товар не найден"} )
        except Exception as e:
            return JsonResponse({"success": False, "message": str( e )} )

    return JsonResponse({"success": False, "message": "Неверный метод запроса"})


def del_all(request):
    # Для авторизованых пользователей
    if request.user.is_authenticated:
        basket = Basket.objects.get(user=request.user)
    # Для анонимных пользователей
    else:
        basket_id = request.session.get('basket_id')
        basket = Basket.objects.get(id=basket_id)
    if basket:
        basket.clear()
    else:
        return redirect('products:index')
    return redirect('products:index')