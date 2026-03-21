from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Product


def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, "shop/shop.html", context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, "shop/product_detail.html", context)