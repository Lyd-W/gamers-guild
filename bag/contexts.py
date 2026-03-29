from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product

def bag_contents(request):
    
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    
    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        
        # CASE 1: Product has no sizes, item_data is just quantity
        if isinstance(item_data, int):
            quantity = item_data
            subtotal = quantity * product.price
            total += quantity * product.price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'subtotal': subtotal
            })
        
        # CASE 2: Product has sizes, item_data is a dict with 'items_by_size'
        else:
            for size, quantity in item_data.get('items_by_size', {}).items():
                subtotal = quantity * product.price
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'subtotal': subtotal,
                    'size': size,  # pass the size to template
                })
    
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0')
        free_delivery_delta = Decimal('0')
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    
    return context