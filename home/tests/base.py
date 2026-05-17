# home/tests/base.py

from django.test import TestCase
from django.contrib.auth.models import User
from home.models import Boardgame, Genre


class BaseTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="user",
            password="pass"
        )

        self.staff = User.objects.create_user(
            username="staff",
            password="pass",
            is_staff=True
        )

        self.genre1 = Genre.objects.create(name="Strategy")
        self.genre2 = Genre.objects.create(name="Family")

        self.game1 = Boardgame.objects.create(
            title="Catan",
            slug="catan",
            author=self.user,
            description="Trading game",
            release_year=2000,
            playtime=60,
            min_players=2,
            max_players=4,
            min_age=10
        )

        self.game1.genres.add(self.genre1)

        self.game2 = Boardgame.objects.create(
            title="Azul",
            slug="azul",
            author=self.user,
            description="Tile game",
            release_year=2018,
            playtime=45,
            min_players=2,
            max_players=4,
            min_age=8
        )