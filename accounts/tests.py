from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class LoginViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='victor', password='secret123')

    def test_invalid_login_shows_form_errors(self):
        response = self.client.post(reverse('login'), {
            'username': 'victor',
            'password': 'wrong-password',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Por favor, entre com um usuário')

    def test_valid_login_redirects_to_cars(self):
        response = self.client.post(reverse('login'), {
            'username': 'victor',
            'password': 'secret123',
        })

        self.assertRedirects(response, reverse('cars_list'))
