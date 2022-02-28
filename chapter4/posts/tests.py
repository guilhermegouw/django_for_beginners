from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTests(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text="Test post text")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.text, "Test post text")


class HomepageViewTests(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text="This is another test")

    def test_homepage_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
