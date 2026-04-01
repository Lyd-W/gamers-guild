from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib import messages
from shop.models import Product, ProductSize


def view_bag(request):

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    item_id = str(item_id)

    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    size = request.POST.get('product_size')
    bag = request.session.get('bag', {})

    if size:
        product_size = get_object_or_404(
            ProductSize, product=product, size=size)

        if quantity > product_size.stock:
            quantity = product_size.stock

        if item_id in bag:
            if isinstance(bag.get(item_id), dict) and 'items_by_size' in bag[item_id]:
                if size in bag[item_id]['items_by_size']:
                    bag[item_id]['items_by_size'][size] += quantity
                else:
                    bag[item_id]['items_by_size'][size] = quantity
            else:
                bag[item_id] = {'items_by_size': {size: quantity}}
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}

    else:
        if item_id in bag:
            if isinstance(bag.get(item_id), dict) and 'items_by_size' in bag[item_id]:
                total_quantity = sum(bag[item_id]['items_by_size'].values()) + quantity
                bag[item_id] = total_quantity
            else:
                bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag

    if size:
        messages.success(request,
                         f'Successfully addded {product.name} (Size: {size}) to your bag!'
                         )
    else:
        messages.success(request,
                         f'Successfully addded {product.name} to your bag!'
                         )
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    item_id = str(item_id)

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    if size:
        messages.info(request,
                      f'Successfully updated quantity of {product.name} (Size: {size}) in your bag!'
                      )
    else:
        messages.info(request,
                      f'Successfully updated quantity of {product.name} in your bag!'
                      )
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    item_id = str(item_id)

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        if size:
            messages.success(request,
                             f'Successfully removed {product.name} (Size: {size}) from your bag!'
                             )
        else:
            messages.success(request,
                             f'Successfully removed {product.name} from your bag!'
                             )
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e} from bag, please try again.')
        return HttpResponse(status=500)
