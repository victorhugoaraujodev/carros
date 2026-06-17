from decimal import Decimal

from django.test import TestCase

from cars.forms import CarModelForm
from cars.models import Brand, Car, CarInventory


class CarFormTests(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Toyota')

    def test_rejects_low_value(self):
        form = CarModelForm(data={
            'model': 'Corolla',
            'brand': self.brand.pk,
            'factory_year': 2020,
            'model_year': 2021,
            'plate': 'ABC1234',
            'value': '19999.99',
            'bio': 'Carro bom',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('value', form.errors)

    def test_rejects_old_factory_year(self):
        form = CarModelForm(data={
            'model': 'Corolla',
            'brand': self.brand.pk,
            'factory_year': 1974,
            'model_year': 1975,
            'plate': 'ABC1234',
            'value': '20000.00',
            'bio': 'Carro antigo',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('factory_year', form.errors)


class CarInventorySignalTests(TestCase):
    def test_creates_inventory_snapshot_on_save_and_delete(self):
        brand = Brand.objects.create(name='Honda')
        car = Car.objects.create(
            model='Civic',
            brand=brand,
            factory_year=2022,
            model_year=2023,
            plate='XYZ9A87',
            value=Decimal('85000.00'),
        )

        latest_inventory = CarInventory.objects.first()
        self.assertEqual(latest_inventory.cars_count, 1)
        self.assertEqual(latest_inventory.cars_value, Decimal('85000.00'))

        car.delete()

        latest_inventory = CarInventory.objects.first()
        self.assertEqual(CarInventory.objects.count(), 2)
        self.assertEqual(latest_inventory.cars_count, 0)
        self.assertEqual(latest_inventory.cars_value, Decimal('0.00'))
