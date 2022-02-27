from http import client
from urllib import response
from django.test import TestCase


class SimpleTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_aboutpage_status_code(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)
