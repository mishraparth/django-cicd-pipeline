from django.test import TestCase
from django.urls import reverse

class PageTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_posts_page(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
