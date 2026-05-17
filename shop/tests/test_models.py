from django.test import TestCase
from shop.models import Product, Category, ProductSize


class ProductModelTests(TestCase):

    def setUp(self):
        self.cat = Category.objects.create(type="board_games")

    def test_product_string_representation(self):
        product = Product.objects.create(
            name="Catan",
            price=20.00,
            stock=5,
            category=self.cat
        )
        self.assertEqual(str(product), "Catan")

    def test_is_in_stock_without_sizes(self):
        product = Product.objects.create(
            name="Chess Set",
            price=10.00,
            stock=5,
            category=self.cat
        )
        self.assertTrue(product.is_in_stock)

    def test_is_in_stock_false(self):
        product = Product.objects.create(
            name="Out of stock item",
            price=10.00,
            stock=0,
            category=self.cat
        )
        self.assertFalse(product.is_in_stock)


class ProductSizeTests(TestCase):

    def setUp(self):
        self.cat = Category.objects.create(type="apparel")
        self.product = Product.objects.create(
            name="T-Shirt",
            price=10.00,
            has_sizes=True,
            category=self.cat
        )

    def test_size_stock_affects_availability(self):
        ProductSize.objects.create(
            product=self.product,
            size="M",
            stock=0
        )

        self.assertFalse(self.product.is_in_stock)