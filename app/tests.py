from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from cars.models import Brand, Car


class HomePageTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='victor', password='secret123')
        self.brand = Brand.objects.create(name='Ford')
        self.car = Car.objects.create(
            model='Fiesta',
            brand=self.brand,
            factory_year=2018,
            model_year=2019,
            plate='AAA1A01',
            value='45000.00',
            bio='Teste',
        )

    def test_home_redirects_anonymous_users_to_login(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_home_loads_for_authenticated_users(self):
        self.client.login(username='victor', password='secret123')

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Buscar carro')

    def test_cars_list_redirects_anonymous_users(self):
        response = self.client.get(reverse('cars_list'))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_car_detail_redirects_anonymous_users(self):
        response = self.client.get(reverse('car_detail', kwargs={'pk': self.car.pk}))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)
