from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower


def all_products(request):

    products = Product.objects.all()

    query = None
    selected_categories = []
    sort = None
    direction = None

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

    if selected_categories:   
        categories = Category.objects.filter(type__in=selected_categories)

        expanded_categories = []

        for cat in categories:
            if cat.subcategories.exists():
                expanded_categories.extend(
                    list(cat.subcategories.values_list('type', flat=True))
                )
            else:
                expanded_categories.append(cat.type)

        selected_categories = expanded_categories

        products = products.filter(category__type__in=selected_categories)
        
        selected_categories = selected_categories

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey

        if sortkey == 'name':
            sortkey = 'lower_name'
            products = products.annotate(lower_name=Lower('name'))

        elif sortkey.startswith('category'):
            products = products.annotate(
                lower_category=Lower('category__readable_type')
            )
            sortkey = 'lower_category'

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'

        products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    categories = Category.objects.filter(parent__isnull=False)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': selected_categories,
        'categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, "shop/shop.html", context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, "shop/product_detail.html", context)
