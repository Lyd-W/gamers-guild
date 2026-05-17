from home.tests.base import BaseTestCase
from home.models import Review


class ReviewTests(BaseTestCase):

    def test_create_review(self):
        self.client.login(username="user", password="pass")

        response = self.client.post(f"/{self.game1.slug}/", {
            "rating": 5,
            "comment": "Excellent"
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Review.objects.filter(boardgame=self.game1).exists()
        )

    def test_review_requires_login(self):
        response = self.client.post(f"/{self.game1.slug}/", {
            "rating": 5,
            "comment": "Nice"
        })

        self.assertEqual(response.status_code, 302)