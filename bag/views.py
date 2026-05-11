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
    if product.has_sizes and not size:
        messages.warning(request, "Please select a valid size.")
        return redirect(redirect_url)
    
    bag = request.session.get('bag', {})

    if size:

        product_size = get_object_or_404(
            ProductSize,
            product=product,
            size=size
        )

        if product_size.stock <= 0:
            messages.warning(
                request,
                f"{product.name} ({size}) is out of stock."
            )
            return redirect(redirect_url)

        current_quantity = 0

        if (
            item_id in bag and
            isinstance(bag.get(item_id), dict) and
            'items_by_size' in bag[item_id] and
            size in bag[item_id]['items_by_size']
        ):
            current_quantity = bag[item_id]['items_by_size'][size]

        if current_quantity + quantity > product_size.stock:

            remaining_stock = product_size.stock - current_quantity

            if remaining_stock <= 0:
                messages.warning(
                    request,
                    f"You already have all available stock of {product.name} ({size}) in your bag."
                )
                return redirect(redirect_url)

            messages.warning(
                request,
                f"Only {remaining_stock} more of {product.name} ({size}) available."
            )

            quantity = remaining_stock

        if item_id in bag:
            if (
                isinstance(bag.get(item_id), dict) and
                'items_by_size' in bag[item_id]
            ):
                if size in bag[item_id]['items_by_size']:
                    bag[item_id]['items_by_size'][size] += quantity
                else:
                    bag[item_id]['items_by_size'][size] = quantity
            else:
                bag[item_id] = {'items_by_size': {size: quantity}}
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}

    else:

        if product.stock <= 0:
            messages.warning(
                request,
                f"{product.name} is out of stock."
            )
            return redirect(redirect_url)

        current_quantity = bag.get(item_id, 0)

        if current_quantity + quantity > product.stock:

            remaining_stock = product.stock - current_quantity

            if remaining_stock <= 0:
                messages.warning(
                    request,
                    f"You already have all available stock of {product.name} in your bag."
                )
                return redirect(redirect_url)

            messages.warning(
                request,
                f"Only {remaining_stock} more of {product.name} available."
            )

            quantity = remaining_stock

        if item_id in bag:
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag

    if size:
        messages.success(
            request,
            f'Successfully added {product.name} (Size: {size}) to your bag!'
        )
    else:
        messages.success(
            request,
            f'Successfully added {product.name} to your bag!'
        )

    return redirect(redirect_url)


def adjust_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    item_id = str(item_id)

    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size')
    bag = request.session.get('bag', {})

    if size:

        product_size = get_object_or_404(
            ProductSize,
            product=product,
            size=size
        )

        if quantity > product_size.stock:
            quantity = product_size.stock

            messages.warning(
                request,
                f"Only {product_size.stock} available for {product.name} ({size})."
            )

        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]

            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)

    else:

        if quantity > product.stock:
            quantity = product.stock

            messages.warning(
                request,
                f"Only {product.stock} available for {product.name}."
            )

        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag

    if size:
        messages.info(
            request,
            f'Successfully updated quantity of {product.name} (Size: {size}) in your bag!'
        )
    else:
        messages.info(
            request,
            f'Successfully updated quantity of {product.name} in your bag!'
        )

    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    item_id = str(item_id)

    try:
        size = request.POST.get('product_size')
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]

            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)

            messages.success(
                request,
                f'Successfully removed {product.name} (Size: {size}) from your bag!'
            )

        else:
            bag.pop(item_id)

            messages.success(
                request,
                f'Successfully removed {product.name} from your bag!'
            )

        request.session['bag'] = bag

        return HttpResponse(status=200)

    except Exception as e:

        messages.warning(
            request,
            f'Error removing item: {e} from bag, please try again.'
        )

        return HttpResponse(status=500)