from django.test import TestCase
from decimal import Decimal
from checkout.models import Order, OrderLineItem
from shop.models import Product, ProductSize


class CheckoutSignalTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Game",
            price=Decimal("10.00"),
            stock=10
        )

        self.size_product = ProductSize.objects.create(
            product=self.product,
            size="M",
            stock=5
        )

        self.order = Order.objects.create(
            full_name="John Doe",
            email="john@example.com",
            phone_number="123",
            street_address1="Test",
            town_or_city="London",
            country="GB",
        )

    def test_stock_reduction_simple_product(self):
        OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2
        )

        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 8)

    def test_stock_reduction_size_product(self):
        OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            product_size="M",
            quantity=2
        )

        self.size_product.refresh_from_db()
        self.assertEqual(self.size_product.stock, 3)