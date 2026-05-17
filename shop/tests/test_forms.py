from django.test import TestCase
from shop.forms import ProductForm
from shop.models import Category


class ProductFormTests(TestCase):

    def setUp(self):
        self.cat = Category.objects.create(type="board_games")

    def test_valid_form(self):
        form = ProductForm(data={
        "name": "Catan",
        "price": 20.00,
        "category": self.cat.id,
        "stock": 5,
        "sku": "CATAN-001",
        "has_sizes": False,
        })

        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_name(self):
        form = ProductForm(data={
            "price": 20.00,
            "category": self.cat.id
        })

        self.assertFalse(form.is_valid())