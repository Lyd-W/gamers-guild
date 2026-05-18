from home.tests.base import BaseTestCase
from home.models import Review


class BoardgameDetailTests(BaseTestCase):

    def setUp(self):
        super().setUp()

        self.review = Review.objects.create(
            boardgame=self.game1,
            user=self.user,
            rating=5,
            comment="Great!",
            is_approved=True
        )

    def test_detail_page_loads(self):
        response = self.client.get(f"/{self.game1.slug}/")
        self.assertEqual(response.status_code, 200)

    def test_reviews_visible_to_anonymous(self):
        self.client.logout()
        response = self.client.get(f"/{self.game1.slug}/")

        self.assertEqual(len(response.context["reviews"]), 1)

    def test_staff_sees_all_reviews(self):
        self.client.login(username="staff", password="pass")
        response = self.client.get(f"/{self.game1.slug}/")

        self.assertIn(self.review, response.context["reviews"])

    def test_authenticated_user_sees_their_unapproved_review(self):

        Review.objects.all().delete()

        Review.objects.create(
            boardgame=self.game1,
            user=self.user,
            rating=4,
            is_approved=False
        )

        self.client.login(username="user", password="pass")
        response = self.client.get(f"/{self.game1.slug}/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["reviews"]), 1)
