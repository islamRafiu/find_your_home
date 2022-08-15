from django.test import TestCase
from django.urls import reverse


class BaseTest(TestCase):
    def setUp(self):
        self.index_url = reverse('index')
        self.about_url = reverse('about')
        return super().setUp()


class IndexTest(BaseTest):
    def test_can_access_index_page(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')


class AboutTest(BaseTest):
    def test_can_access_about_page(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')
