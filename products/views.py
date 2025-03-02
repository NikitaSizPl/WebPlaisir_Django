from .models import Catigories, Product
from django.shortcuts import render


def categories(request):
    categor = Catigories.objects.all()
    context = {
        "categor": categor
    }
    return render(request,
                  "products/categories.html",
                  context
                  )


def items_categor(request, cat_name):
    categor = Catigories.objects.get(name=cat_name)
    products = Product.objects.filter(categories__name=cat_name)
    context = {
        'products': products,
        'categor': categor
    }
    return render(request,
                  "products/items_categor.html",
                  context
                  )


def product_id(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request,
                  "products/product_id.html",
                  context
                  )


def index(request):
    items = Product.objects.all()
    categor = Catigories.objects.all()
    tort_all = Product.objects.filter(categories__name='torty')
    macarons_all = Product.objects.filter(categories__name='macarons')
    сroissants_all = Product.objects.filter(categories__name='сroissants')
    context = {
        'items': items,
        'categor': categor,
        'tort_all': tort_all,
        'macarons_all': macarons_all,
        'сroissants_all': сroissants_all
    }
    return render(request,
                  'products/index.html',
                  context
                  )