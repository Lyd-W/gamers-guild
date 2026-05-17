from django.test import TestCase, RequestFactory
from checkout.webhook_handler import StripeWH_Handler
from checkout.models import Order
from decimal import Decimal


class WebhookPaymentSuccessTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.post("/")
        self.handler = StripeWH_Handler(self.request)

        self.order = Order.objects.create(
            full_name="John Doe",
            email="john@example.com",
            phone_number="123",
            street_address1="1 Street",
            town_or_city="London",
            country="GB",
            grand_total=Decimal("10.00"),
            original_bag="{}",
            stripe_pid="pi_test_123"
        )

    def test_handle_event_returns_200(self):
        response = self.handler.handle_event({"type": "random.event"})
        self.assertEqual(response.status_code, 200)