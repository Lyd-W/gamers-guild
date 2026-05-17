from home.tests.base import BaseTestCase


class SearchViewTests(BaseTestCase):

    def test_search_returns_boardgames(self):
        response = self.client.get("/search/?q=Catan")
        self.assertContains(response, "Catan")

    def test_search_returns_products_page(self):
        response = self.client.get("/search/?q=test")
        self.assertEqual(response.status_code, 200)

    def test_empty_query_returns_no_results(self):
        response = self.client.get("/search/")
        self.assertEqual(len(response.context["boardgames"]), 0)