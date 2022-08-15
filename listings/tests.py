from django.test import TestCase
import requests
from django.urls import reverse


class BaseTest(TestCase):
    def setUp(self):
        self.index_url = reverse('listings')
        return super().setUp()


class IndexTest(BaseTest):
    def test_can_access_index_page(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listing/listings.html')


class ListingTest(BaseTest):
    def test_listing_existed(self):
        response = requests.get('http://127.0.0.1:8000/admin/listings/listing/add/')
        self.assertEqual(response.status_code, 200)

