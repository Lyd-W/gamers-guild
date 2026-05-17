from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem
from shop.models import ProductSize


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()

    if created:

        if instance.product_size:

            try:
                product_size = ProductSize.objects.get(
                    product=instance.product,
                    size=instance.product_size
                )

                if product_size.stock >= instance.quantity:
                    product_size.stock -= instance.quantity
                else:
                    product_size.stock = 0

                product_size.save()

            except ProductSize.DoesNotExist:
                pass


@receiver(post_save, sender=OrderLineItem)
def reduce_simple_stock(sender, instance, created, **kwargs):
    if created and not instance.product_size:
        product = instance.product
        product.stock = max(0, product.stock - instance.quantity)
        product.save()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    instance.order.update_total()
