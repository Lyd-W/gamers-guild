from decimal import Decimal
from django.test import TestCase, RequestFactory
from django.conf import settings
from bag.contexts import bag_contents
from shop.models import Product, Category


class BagContextTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        self.category = Category.objects.create(type="boardgame")

        self.product = Product.objects.create(
            name="Catan",
            price=10,
            category=self.category,
            stock=10
        )

    def test_total_calculation(self):
        request = self.factory.get("/")
        request.session = {"bag": {str(self.product.id): 2}}

        context = bag_contents(request)

        self.assertEqual(context["total"], 20)
        self.assertEqual(context["product_count"], 2)

    def test_delivery_calculation(self):
        request = self.factory.get("/")
        request.session = {"bag": {str(self.product.id): 1}}

        context = bag_contents(request)

        expected_delivery = Decimal(
            10 * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        )

        self.assertEqual(context["delivery"], expected_delivery)

    def test_free_delivery_threshold(self):
        expensive = Product.objects.create(
            name="Expensive Game",
            price=settings.FREE_DELIVERY_THRESHOLD + 10,
            category=self.category,
            stock=5
        )

        request = self.factory.get("/")
        request.session = {"bag": {str(expensive.id): 1}}

        context = bag_contents(request)

        self.assertEqual(context["free_delivery_delta"], Decimal("0"))