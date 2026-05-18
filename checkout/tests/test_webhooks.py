from django.test import TestCase, RequestFactory
from checkout.webhook_handler import StripeWH_Handler


class WebhookHandlerTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.post("/")
        self.handler = StripeWH_Handler(self.request)

    def test_handle_event_default(self):
        response = self.handler.handle_event({"type": "unknown.event"})
        self.assertEqual(response.status_code, 200)
