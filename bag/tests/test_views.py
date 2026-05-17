from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Product, Category, ProductSize


class BagViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.category = Category.objects.create(type="boardgame")

        self.product = Product.objects.create(
            name="Catan",
            price=10,
            category=self.category,
            stock=5,
            has_sizes=False
        )

        self.size_product = Product.objects.create(
            name="Hoodie",
            price=20,
            category=self.category,
            stock=0,
            has_sizes=True
        )

        self.size_m = ProductSize.objects.create(
            product=self.size_product,
            size="M",
            stock=3
        )

    def test_view_bag_renders(self):
        response = self.client.get(reverse("view_bag"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bag/bag.html")

    def test_add_simple_product_to_bag(self):
        self.client.post(
            reverse("add_to_bag", args=[self.product.id]),
            {"quantity": 2, "redirect_url": "/"}
        )

        bag = self.client.session["bag"]

        self.assertEqual(bag[str(self.product.id)], 2)

    def test_add_respects_stock_limit(self):
        self.client.post(
            reverse("add_to_bag", args=[self.product.id]),
            {"quantity": 999, "redirect_url": "/"}
        )

        bag = self.client.session["bag"]

        self.assertEqual(bag[str(self.product.id)], 5)

    def test_add_size_product(self):
        self.client.post(
            reverse("add_to_bag", args=[self.size_product.id]),
            {
                "quantity": 2,
                "product_size": "M",
                "redirect_url": "/"
            }
        )

        bag = self.client.session["bag"]

        self.assertEqual(
            bag[str(self.size_product.id)]["items_by_size"]["M"],
            2
        )

    def test_size_product_requires_size(self):
        self.client.post(
            reverse("add_to_bag", args=[self.size_product.id]),
            {
                "quantity": 1,
                "redirect_url": "/"
            }
        )

        session = self.client.session

        bag = session.get("bag", {})

        self.assertEqual(bag, {})

    def test_adjust_simple_product(self):
        self.client.post(
            reverse("add_to_bag", args=[self.product.id]),
            {"quantity": 2, "redirect_url": "/"}
        )

        self.client.post(
            reverse("adjust_bag", args=[self.product.id]),
            {"quantity": 4}
        )

        bag = self.client.session["bag"]

        self.assertEqual(bag[str(self.product.id)], 4)

    def test_adjust_clamps_to_stock(self):
        self.client.post(
            reverse("add_to_bag", args=[self.product.id]),
            {"quantity": 1, "redirect_url": "/"}
        )

        self.client.post(
            reverse("adjust_bag", args=[self.product.id]),
            {"quantity": 999}
        )

        bag = self.client.session["bag"]

        self.assertEqual(bag[str(self.product.id)], 5)

    def test_remove_simple_product(self):
        self.client.post(
            reverse("add_to_bag", args=[self.product.id]),
            {"quantity": 1, "redirect_url": "/"}
        )

        response = self.client.post(
            reverse("remove_from_bag", args=[self.product.id]),
            {}
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotIn(str(self.product.id), self.client.session["bag"])

    def test_remove_size_product(self):
        self.client.post(
            reverse("add_to_bag", args=[self.size_product.id]),
            {
                "quantity": 2,
                "product_size": "M",
                "redirect_url": "/"
            }
        )

        self.client.post(
            reverse("remove_from_bag", args=[self.size_product.id]),
            {"product_size": "M"}
        )

        bag = self.client.session["bag"]

        self.assertNotIn(str(self.size_product.id), bag)

    def test_empty_bag_structure(self):
        response = self.client.get(reverse("view_bag"))
        self.assertEqual(response.status_code, 200)