from django.test import TestCase
from django.urls import reverse
from shop.models import Product, Category


class ShopFilterTests(TestCase):

    def setUp(self):
        self.parent = Category.objects.create(type="games")
        self.child = Category.objects.create(
            type="board_games",
            parent=self.parent
        )

        Product.objects.create(
            name="Catan",
            price=10,
            category=self.child
        )

        Product.objects.create(
            name="Chess",
            price=5,
            category=self.child
        )

    def test_category_filter(self):
        url = reverse("shop") + "?category=board_games"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Catan")

    def test_parent_filter(self):
        url = reverse("shop") + "?parent=games"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
