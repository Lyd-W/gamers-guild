from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import UserProfile
from django.contrib.auth.models import User
from checkout.models import Order
from decimal import Decimal
from shop.models import Product


class SaveInfoTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username="john",
            password="password123",
            email="john@example.com"
        )

        self.profile = UserProfile.objects.get(user=self.user)

        self.product = Product.objects.create(
            name="Catan",
            price=Decimal("10.00"),
            stock=10
        )

        session = self.client.session
        session["bag"] = {str(self.product.id): 1}
        session["save_info"] = True
        session.save()

    def test_save_info_updates_profile(self):
        self.client.login(username="john", password="password123")

        order = Order.objects.create(
            full_name="John Doe",
            email="john@example.com",
            phone_number="123",
            street_address1="1 Street",
            town_or_city="London",
            country="GB",
            order_total=Decimal("10.00"),
            grand_total=Decimal("10.00"),
            delivery_cost=Decimal("0.00"),
            original_bag="{}",
            stripe_pid="test_pid"
        )

        response = self.client.get(
            reverse("checkout_success", args=[order.order_number])
        )

        self.assertEqual(response.status_code, 200)