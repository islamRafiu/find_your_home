from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


# Base Test Case for creating user with different attributes
class BaseTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.registration_url = reverse('register')
        self.dashboard_url = reverse('dashboard')
        self.user = {
            'first_name':'first',
            'last_name': 'last',
            'username': 'username',
            'email': 'testemail@gmail.com',
            'password':'password',
            'password2':'password'
        }
        return super().setUp()


class LoginTest(BaseTest):
    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'accounts/login.html')

    def test_login_success(self):
        self.client.post(self.registration_url, self.user, format='text/html')
        user = User.objects.filter(email=self.user['email']).first()
        user.is_active = True
        user.save()
        response = self.client.post(self.login_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 302)


class RegistrationTest(BaseTest):
    def test_registration_success(self):
        response = self.client.get(self.registration_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')


class DashboardTest(BaseTest):
    def test_dashboard_success(self):
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/dashboard.html')
