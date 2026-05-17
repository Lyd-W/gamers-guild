from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from shop.models import Product, Category


class ShopViewTests(TestCase):

    def setUp(self):
        self.cat = Category.objects.create(type="board_games")

        self.product = Product.objects.create(
            name="Catan",
            price=20.00,
            category=self.cat,
            stock=5
        )

    def test_shop_page_loads(self):
        response = self.client.get(reverse("shop"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/shop.html")

    def test_product_detail_page(self):
        response = self.client.get(
            reverse("product_detail", args=[self.product.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Catan")


class AdminProductTests(TestCase):

    def setUp(self):
        self.admin = User.objects.create_superuser(
            username="admin",
            email="admin@test.com",
            password="pass"
        )
        self.cat = Category.objects.create(type="board_games")

    def test_non_admin_cannot_access_add(self):
        response = self.client.get(reverse("add_product"))
        self.assertEqual(response.status_code, 302)

    def test_admin_can_access_add(self):
        self.client.login(username="admin", password="pass")
        response = self.client.get(reverse("add_product"))
        self.assertEqual(response.status_code, 200)