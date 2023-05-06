from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        self.item = Menu.objects.create(title='Ice Cream', price=1.79, inventory=100)
        self.assertEqual(str(self.item), 'Ice Cream: 1.79')