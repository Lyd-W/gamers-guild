from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from shop.models import Product


class CheckoutEdgeCaseTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.product = Product.objects.create(
            name="Catan",
            price=Decimal("15.00"),
            stock=0
        )

    def test_checkout_redirects_with_empty_bag(self):
        response = self.client.get(reverse("checkout"))
        self.assertEqual(response.status_code, 302)

    def test_checkout_invalid_form(self):
        session = self.client.session
        session["bag"] = {str(self.product.id): 1}
        session.save()

        response = self.client.post(reverse("checkout"), {
            "full_name": "",
            "email": "invalid"
        })

        self.assertEqual(response.status_code, 200)
