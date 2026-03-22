from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):

    products = Product.objects.all()
    categories = Category.objects.all()
    query = None
    selected_categories = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query: 
                messages.error(
                    request,
                    "You didn't say what you were looking for, adventurer"
                )
                return redirect(reverse('shop'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            
        if 'category' in request.GET:
            selected_categories = request.GET.getlist('category')
            products = products.filter(category__type__in=selected_categories)

    context = {
        'products': products,
        'search_term': query,
        'categories': categories,
        'current_categories': selected_categories,
    }

    return render(request, "shop/shop.html", context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, "shop/product_detail.html", context)