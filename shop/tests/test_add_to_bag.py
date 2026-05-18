from django.test import TestCase
from django.urls import reverse
from shop.models import Product, Category


class BagTests(TestCase):

    def setUp(self):
        self.cat = Category.objects.create(type="games")
        self.product = Product.objects.create(
            name="Catan",
            price=20,
            stock=10,
            category=self.cat
        )

    def test_add_to_bag_post(self):
        self.client.post(
            reverse("add_to_bag", args=[self.product.id]),
            {
                "quantity": 2,
                "redirect_url": "/shop/"
            }
        )

        bag = self.client.session.get("bag", {})
        self.assertEqual(bag[str(self.product.id)], 2)
