from home.tests.base import BaseTestCase
from home.models import Review


class PermissionTests(BaseTestCase):

    def setUp(self):
        super().setUp()

        self.review = Review.objects.create(
            boardgame=self.game1,
            user=self.user,
            rating=5
        )

    def test_only_staff_can_approve_review(self):
        self.client.login(username="user", password="pass")

        response = self.client.post(
            f"/review/{self.review.id}/approve/"
        )

        self.review.refresh_from_db()
        self.assertFalse(self.review.is_approved)

    def test_staff_can_approve_review(self):
        self.client.login(username="staff", password="pass")

        response = self.client.post(
            f"/review/{self.review.id}/approve/"
        )

        self.review.refresh_from_db()
        self.assertTrue(self.review.is_approved)

    def test_toggle_favourite_requires_login(self):
        response = self.client.post(f"/{self.game1.slug}/favourite/")
        self.assertEqual(response.status_code, 302)