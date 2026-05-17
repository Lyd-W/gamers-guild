from django.test import TestCase

from django.test import TestCase
from django.urls import reverse


class AboutViewTests(TestCase):

    def test_about_page_loads(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about/about.html")

    def test_contact_form_in_context(self):
        response = self.client.get(reverse("about"))

        self.assertIn("form", response.context)

    def test_valid_contact_form_submission(self):
        response = self.client.post(
            reverse("about"),
            {
                "name": "Test User",
                "email": "test@test.com",
                "subject": "Test Subject",
                "message": "Test message",
            },
            follow=True
        )

        self.assertEqual(response.status_code, 200)

        messages = list(response.context["messages"])

        self.assertTrue(
            any(
                "Your message has been sent successfully!"
                in str(message)
                for message in messages
            )
        )

    def test_invalid_contact_form_submission(self):
        response = self.client.post(
            reverse("about"),
            {
                "name": "",
                "email": "not-an-email",
                "subject": "",
                "message": "",
            }
        )

        self.assertEqual(response.status_code, 200)

        form = response.context["form"]

        self.assertTrue(form.errors)