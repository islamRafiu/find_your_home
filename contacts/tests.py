from django.test import TestCase
import requests


class BaseTest(TestCase):

    def setUp(self):
        return super().setUp()


class ContactsTest(BaseTest):
    def valid_contacts(self):
        response = requests.get('http://127.0.0.1:8000/listings/5')
        self.assertEqual(response.status_code, 200)
