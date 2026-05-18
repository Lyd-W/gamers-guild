from home.tests.base import BaseTestCase


class HomeViewTests(BaseTestCase):

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_games_displayed(self):
        response = self.client.get("/")
        self.assertIn(self.game1, response.context["boardgames"])

    def test_filter_by_genre(self):
        response = self.client.get("/", {"genre": self.genre1.id})
        self.assertIn(self.game1, response.context["boardgames"])

    def test_filter_by_players(self):
        response = self.client.get("/", {"players": "3"})
        self.assertEqual(response.status_code, 200)

    def test_filter_by_playtime(self):
        response = self.client.get("/", {"playtime": 50})
        self.assertIn(self.game2, response.context["boardgames"])

    def test_sort_by_title_desc(self):
        response = self.client.get("/", {
            "sort": "title",
            "direction": "desc"
        })

        games = list(response.context["boardgames"])
        self.assertGreaterEqual(games[0].title, games[1].title)

    def test_empty_filter_results(self):
        response = self.client.get("/", {"genre": 9999})
        self.assertEqual(response.status_code, 200)
