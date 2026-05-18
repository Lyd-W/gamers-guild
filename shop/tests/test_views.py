from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from shop.models import Product, Category
from django.contrib.messages import get_messages


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

    def test_empty_search_redirects(self):
        response = self.client.get(reverse("shop"), {"q": ""})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("shop"))

    def test_search_products(self):
        response = self.client.get(reverse("shop"), {"q": "Catan"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Catan")

    def test_sort_products_by_name(self):
        Product.objects.create(
            name="Azul",
            price=10,
            category=self.cat,
            stock=1
        )

        response = self.client.get(
            reverse("shop"),
            {"sort": "name", "direction": "asc"}
        )

        self.assertEqual(response.status_code, 200)

    def test_sort_products_by_category(self):
        response = self.client.get(
            reverse("shop"),
            {"sort": "category", "direction": "asc"}
        )

        self.assertEqual(response.status_code, 200)

    def test_sort_descending(self):
        response = self.client.get(
            reverse("shop"),
            {"sort": "name", "direction": "desc"}
        )

        self.assertEqual(response.status_code, 200)

    def test_category_filter_applies(self):
        response = self.client.get(
            reverse("shop"),
            {"category": "board_games"}
        )

        self.assertEqual(response.status_code, 200)

    def test_parent_filter_applies(self):
        parent = Category.objects.create(type="games")
        child = Category.objects.create(type="board_games", parent=parent)

        Product.objects.create(
            name="Risk",
            price=10,
            category=child,
            stock=5
        )

        response = self.client.get(
            reverse("shop"),
            {"parent": "games"}
        )

        self.assertEqual(response.status_code, 200)

    def test_sort_products_by_category_desc(self):
        response = self.client.get(
            reverse("shop"),
            {"sort": "category", "direction": "desc"}
        )

        self.assertEqual(response.status_code, 200)

    def test_parent_and_category_combined_filter(self):
        parent = Category.objects.create(type="games")
        child = Category.objects.create(type="board_games", parent=parent)

        Product.objects.create(
            name="Catan",
            price=10,
            category=child,
            stock=5
        )

        Product.objects.create(
            name="Chess",
            price=10,
            category=child,
            stock=5
        )

        response = self.client.get(
            reverse("shop"),
            {"parent": "games", "category": "board_games"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Catan")

    def test_subcategory_default_branch(self):
        response = self.client.get(reverse("shop"))

        self.assertEqual(response.status_code, 200)

    def test_category_sort_uses_annotation(self):
        parent = Category.objects.create(type="games")

        child = Category.objects.create(
            type="board_games",
            parent=parent,
            readable_type="Board Games"
        )

        Product.objects.create(
            name="Catan",
            price=10,
            category=child,
            stock=5
        )

        response = self.client.get(
            reverse("shop"),
            {"sort": "category", "direction": "asc"}
        )

        self.assertEqual(response.status_code, 200)

    def test_name_sort_lower_annotation_triggered(self):
        Product.objects.create(
            name="zulu",
            price=10,
            category=self.cat
        )

        Product.objects.create(
            name="alpha",
            price=10,
            category=self.cat
        )

        response = self.client.get(
            reverse("shop"),
            {"sort": "name", "direction": "asc"}
        )

        self.assertEqual(response.status_code, 200)

    def test_empty_search_message(self):
        response = self.client.get(reverse("shop"), {"q": ""})

        messages_list = list(get_messages(response.wsgi_request))

        self.assertTrue(any(
            "didn't say what you were looking for" in str(m)
            for m in messages_list
        ))


class AdminProductTests(TestCase):

    def setUp(self):
        self.admin = User.objects.create_superuser(
            username="admin",
            email="admin@test.com",
            password="pass"
        )
        self.cat = Category.objects.create(type="board_games")

        self.product = Product.objects.create(
            name="Catan",
            price=20,
            category=self.cat,
            stock=5
        )

    def test_non_admin_cannot_access_add(self):
        response = self.client.get(reverse("add_product"))
        self.assertEqual(response.status_code, 302)

    def test_admin_can_access_add(self):
        self.client.login(username="admin", password="pass")
        response = self.client.get(reverse("add_product"))
        self.assertEqual(response.status_code, 200)

    def test_admin_can_post_add_product(self):
        self.client.login(username="admin", password="pass")

        response = self.client.post(reverse("add_product"), {
            "name": "Terraforming Mars",
            "price": 50,
            "category": self.cat.id,
            "stock": 5,
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Product.objects.filter(name="Terraforming Mars").exists()
        )

    def test_invalid_add_product_form(self):
        self.client.login(username="admin", password="pass")

        response = self.client.post(reverse("add_product"), {
            "name": "",
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Failed to add product")

    def test_admin_can_edit_product(self):
        self.client.login(username="admin", password="pass")

        response = self.client.post(
            reverse("edit_product", args=[self.product.id]),
            {
                "name": "Updated Catan",
                "price": 25,
                "category": self.cat.id,
                "stock": 10,
            }
        )

        self.product.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.product.name, "Updated Catan")

    def test_edit_product_page_loads(self):
        self.client.login(username="admin", password="pass")

        response = self.client.get(
            reverse("edit_product", args=[self.product.id])
        )

        self.assertEqual(response.status_code, 200)

    def test_admin_can_delete_product(self):
        self.client.login(username="admin", password="pass")

        response = self.client.get(
            reverse("delete_product", args=[self.product.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Product.objects.filter(id=self.product.id).exists()
        )

    def test_non_admin_cannot_edit_product(self):
        response = self.client.get(
            reverse("edit_product", args=[self.product.id])
        )

        self.assertEqual(response.status_code, 302)

    def test_non_admin_cannot_delete_product(self):
        response = self.client.get(
            reverse("delete_product", args=[self.product.id])
        )

        self.assertEqual(response.status_code, 302)
