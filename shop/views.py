from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Product


def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, "shop/shop.html", context)