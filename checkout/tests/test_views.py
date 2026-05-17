from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from shop.models import Product
from checkout.models import Order


class CheckoutViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.product = Product.objects.create(
            name="Test Game",
            price=Decimal("10.00"),
            stock=10
        )

        session = self.client.session
        session["bag"] = {
            str(self.product.id): 2
        }
        session.save()

    def test_checkout_page_loads(self):
        response = self.client.get(reverse("checkout"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout.html")

    def test_empty_bag_redirects(self):
        session = self.client.session
        session.clear()
        session.save()

        response = self.client.get(reverse("checkout"))

        self.assertEqual(response.status_code, 302)

    def test_checkout_success_view(self):
        order = Order.objects.create(
            order_number="TEST123",
            full_name="Test User",
            email="test@test.com",
            phone_number="123",
            country="GB",
            postcode="SW1",
            town_or_city="London",
            street_address1="Test St",
        )

        response = self.client.get(reverse("checkout_success", args=[order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")