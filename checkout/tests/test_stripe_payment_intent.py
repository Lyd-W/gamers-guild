from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from unittest.mock import patch
from shop.models import Product


class StripeIntentTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.product = Product.objects.create(
            name="Catan",
            price=Decimal("20.00"),
            stock=10
        )

        session = self.client.session
        session["bag"] = {str(self.product.id): 1}
        session.save()

    @patch("stripe.PaymentIntent.create")
    def test_payment_intent_created(self, mock_intent):
        mock_intent.return_value.client_secret = "test_secret"

        response = self.client.get(reverse("checkout"))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(mock_intent.called)
