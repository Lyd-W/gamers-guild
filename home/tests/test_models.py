from django.core.exceptions import ValidationError
from home.tests.base import BaseTestCase
from home.models import Review
from django.db import IntegrityError


class ModelTests(BaseTestCase):

    def test_boardgame_str(self):
        self.assertEqual(str(self.game1), "Catan")

    def test_review_str(self):
        review = Review.objects.create(
            boardgame=self.game1,
            user=self.user,
            rating=5
        )
        self.assertIn("Catan", str(review))

    def test_min_players_validation(self):
        game = self.game1
        game.min_players = 5
        game.max_players = 2

        with self.assertRaises(ValidationError):
            game.clean()

    def test_review_unique_constraint(self):
        Review.objects.create(
            boardgame=self.game1,
            user=self.user,
            rating=4
        )

        with self.assertRaises(IntegrityError):
            Review.objects.create(
                boardgame=self.game1,
                user=self.user,
                rating=5
            )