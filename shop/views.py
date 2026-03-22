from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower


def all_products(request):

    products = Product.objects.all()
    query = None
    selected_categories = None
    sort = None
    direction = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You didn't say what you were looking for, adventurer"
                )
                return redirect(reverse('shop'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

        if 'category' in request.GET:
            selected_categories = request.GET['category'].split(',')
            categories = Category.objects.filter(type__in=selected_categories)
            subcategories = Category.objects.filter(parent__in=categories)
            all_categories = categories | subcategories
            all_category_types = [cat.type for cat in all_categories]
            products = products.filter(category__type__in=all_category_types)

        if request.GET:
            if 'sort' in request.GET:
                sortkey = request.GET['sort']
                sort = sortkey
                if sortkey == 'name':
                    sortkey = 'lower_name'
                    products = products.annotate(lower_name=Lower('name'))

                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'

                products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': selected_categories,
        'current_sorting': current_sorting,
    }

    return render(request, "shop/shop.html", context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, "shop/product_detail.html", context)
