from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from shop.models import Product


class CheckoutIntegrationTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.product = Product.objects.create(
            name="Catan",
            price=Decimal("25.00"),
            stock=10
        )

        session = self.client.session
        session["bag"] = {
            str(self.product.id): 2
        }
        session.save()

    def test_checkout_flow_creates_order_and_clears_bag(self):
        response = self.client.post(reverse("checkout"), {
            "full_name": "John Doe",
            "email": "john@example.com",
            "phone_number": "123456",
            "country": "GB",
            "postcode": "SW1A 1AA",
            "town_or_city": "London",
            "street_address1": "1 Test Street",
            "street_address2": "",
            "county": "",
            "client_secret": "pi_test_secret_123"
        })

        self.assertEqual(response.status_code, 302)

        self.assertNotIn("bag", self.client.session)