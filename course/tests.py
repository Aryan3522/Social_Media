from django.test import TestCase
from django.urls import reverse
from .models import Signup

class LoginTests(TestCase):
    def setUp(self):
        # Create a normal user
        self.user = Signup.objects.create_user(
            email='a@gmail.com',
            password='1234',
            firstName='Aryan'
        )
        # Create a superuser
        self.superuser = Signup.objects.create_superuser(
            email='aryan@gmail.com',
            password='1234',
            firstName='Aryan'
        )

    def test_normal_user_login(self):
        response = self.client.post(reverse('login'), {
            'email': 'a@gmail.com',
            'password': '1234'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertFalse(self.client.session.get('is_superuser'))  # Check if is_superuser is False

    def test_remember_me_checked(self):
        response = self.client.post(reverse('login'), {
            'email': 'a@gmail.com',
            'password': '1234',
            'remember_me': 'on'  # Simulate checking the "remember me" checkbox
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertEqual(self.client.session.get_expiry_age(), 60 * 60 * 24 * 30)  # Check if session expires in 30 days

    def test_remember_me_not_checked(self):
        response = self.client.post(reverse('login'), {
            'email': 'a@gmail.com',
            'password': '1234',
            'remember_me': ''  # Simulate not checking the "remember me" checkbox
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertEqual(self.client.session.get_expiry_age(), 0)  # Check if session expires when browser is closed

        response = self.client.post(reverse('login'), {
            'email': 'aryan@gmail.com',
            'password': '1234'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertTrue(self.client.session.get('is_superuser'))  # Check if is_superuser is True
