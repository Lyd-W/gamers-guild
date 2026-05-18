from django.test import TestCase
from decimal import Decimal
from checkout.models import Order, OrderLineItem
from shop.models import Product


class OrderModelTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Game",
            price=Decimal("10.00"),
            stock=10
        )

        self.order = Order.objects.create(
            full_name="John Doe",
            email="john@example.com",
            phone_number="123456",
            street_address1="1 Test Street",
            town_or_city="London",
            country="GB",
        )

    def test_lineitem_total_calculation(self):
        line = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2
        )

        self.assertEqual(line.lineitem_total, Decimal("20.00"))

    def test_order_update_total(self):
        OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2
        )

        self.order.update_total()
        self.assertEqual(self.order.order_total, Decimal("20.00"))
