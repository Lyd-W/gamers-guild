from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from decimal import Decimal
from profiles.models import UserProfile
from checkout.models import Order
from home.models import Boardgame


class ProfileViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        self.profile = UserProfile.objects.get(user=self.user)

        self.client.login(username="testuser", password="password123")

    def create_boardgame(**kwargs):
        defaults = {
            "title": "Test Game",
            "slug": "test-game",
            "release_year": 2000,
        }
        defaults.update(kwargs)
        return Boardgame.objects.create(**defaults)

    def test_profile_page_loads(self):
        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_profile_update(self):
        response = self.client.post(reverse("profile"), {
            "default_phone_number": "123456",
            "default_town_or_city": "London",
            "default_street_address1": "1 Test Street",
            "default_street_address2": "",
            "default_county": "",
            "default_postcode": "SW1A 1AA",
            "default_country": "GB",
        },
            follow=True
        )

        self.profile.refresh_from_db()

        self.assertEqual(self.profile.default_phone_number, "123456")
        self.assertEqual(response.status_code, 200)

    def test_profile_invalid_update(self):
        response = self.client.post(reverse("profile"), {
            "default_country": "INVALID",
        },
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Could not update your profile")

    def test_favourites_display(self):
        game = Boardgame.objects.create(
            title="Catan",
            slug="catan",
            author=self.user,
            description="Test description",
            release_year=1995,
            playtime=60,
            min_players=2,
            max_players=4,
        )

        self.user.favourite_boardgames.add(game)

        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Catan")


class ProfileOrderHistoryTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        self.profile = UserProfile.objects.get(user=self.user)

        self.client.login(username="testuser", password="password123")

        self.order = Order.objects.create(
            user_profile=self.profile,
            order_number="ABC123",
            full_name="Test User",
            email="test@test.com",
            phone_number="123",
            country="GB",
            postcode="SW1",
            town_or_city="London",
            street_address1="Test Street",
            grand_total=Decimal("50.00"),
        )

    def test_order_appears_in_profile(self):
        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ABC123")


class OrderHistoryViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        self.profile = UserProfile.objects.get(user=self.user)

        self.client.login(username="testuser", password="password123")

        self.order = Order.objects.create(
            user_profile=self.profile,
            order_number="XYZ999",
            full_name="Test User",
            email="test@test.com",
            phone_number="123",
            country="GB",
            postcode="SW1",
            town_or_city="London",
            street_address1="Test Street",
            grand_total=Decimal("75.00"),
        )

    def test_order_history_view(self):
        response = self.client.get(
            reverse("order_history", args=[self.order.order_number])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "checkout/checkout_success.html"
        )


class ProfileOwnershipTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.create_user(
            username="user1",
            password="pass123"
        )
        self.user2 = User.objects.create_user(
            username="user2",
            password="pass123"
        )

        self.profile1 = UserProfile.objects.get(user=self.user1)
        self.profile2 = UserProfile.objects.get(user=self.user2)

    def test_profile_is_user_specific(self):
        self.client.login(username="user1", password="pass123")

        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, 200)

        self.assertNotContains(response, self.user2.username)


class OrderIsolationTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.create_user(
            username="user1",
            password="pass123"
        )
        self.user2 = User.objects.create_user(
            username="user2",
            password="pass123"
        )

        self.profile1 = UserProfile.objects.get(user=self.user1)
        self.profile2 = UserProfile.objects.get(user=self.user2)

        self.order1 = Order.objects.create(
            user_profile=self.profile1,
            order_number="ORDER1",
            full_name="User One",
            email="u1@test.com",
            phone_number="123",
            country="GB",
            postcode="SW1",
            town_or_city="London",
            street_address1="Street 1",
            grand_total=100
        )

        self.order2 = Order.objects.create(
            user_profile=self.profile2,
            order_number="ORDER2",
            full_name="User Two",
            email="u2@test.com",
            phone_number="456",
            country="GB",
            postcode="SW2",
            town_or_city="London",
            street_address1="Street 2",
            grand_total=200
        )

    def test_user_cannot_see_other_users_orders(self):
        self.client.login(username="user1", password="pass123")

        response = self.client.get(reverse("profile"))

        self.assertContains(response, "ORDER1")
        self.assertNotContains(response, "ORDER2")


class FavouriteIsolationTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.create_user(
            username="user1",
            password="pass123"
        )
        self.user2 = User.objects.create_user(
            username="user2",
            password="pass123"
        )

        self.game1 = Boardgame.objects.create(
            title="Catan",
            slug="catan",
            author=self.user1,
            description="Test game",
            release_year=1995,
            playtime=60,
            min_players=2,
            max_players=4,
        )

        self.game2 = Boardgame.objects.create(
            title="Risk",
            slug="risk",
            author=self.user2,
            description="Test game",
            release_year=1959,
            playtime=120,
            min_players=2,
            max_players=6,
        )

    def test_favourites_are_user_specific(self):
        self.user1.favourite_boardgames.add(self.game1)
        self.user2.favourite_boardgames.add(self.game2)

        self.client.login(username="user1", password="pass123")
        response = self.client.get(reverse("profile"))

        self.assertContains(response, "Catan")
        self.assertNotContains(response, "Risk")


class ProfileUpdateIsolationTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.create_user(
            username="user1",
            password="pass123"
        )
        self.user2 = User.objects.create_user(
            username="user2",
            password="pass123"
        )

        self.profile1 = UserProfile.objects.get(user=self.user1)
        self.profile2 = UserProfile.objects.get(user=self.user2)

    def test_profile_update_is_isolated(self):
        self.client.login(username="user1", password="pass123")

        self.client.post(reverse("profile"), {
            "default_phone_number": "999999",
            "default_country": "GB",
        })

        self.profile1.refresh_from_db()
        self.profile2.refresh_from_db()

        self.assertEqual(self.profile1.default_phone_number, "999999")

        self.assertIsNone(self.profile2.default_phone_number)
