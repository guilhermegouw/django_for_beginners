from urllib import response
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user", email="user@testmail.com", password="secret"
        )

        self.post = Post.objects.create(
            title="Interesting post",
            body="Some very informational body",
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title="Some title")
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1')

    def test_post_content(self):
        self.assertEqual(self.post.title, "Interesting post")
        self.assertEqual(self.post.body, "Some very informational body")
        self.assertEqual(self.post.author, self.user)

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Interesting post")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detail_view(self):
        response = self.client.get("http://127.0.0.1:8000/post/1")
        no_response = self.client.get("http://127.0.0.1:8000/post/1000")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Interesting post")
        self.assertTemplateUsed(response, "post_detail.html")

    def test_post_create_view(self):
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "New title",
                "body": "New text",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New text")

    def test_post_update_view(self):
        response = self.client.post(
            reverse("post_edit", args="1"),
            {"title": "Updated title", "body": "Updated text"},
        )
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)
