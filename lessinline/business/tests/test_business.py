from django.test import TestCase
from lessinline.accounts.models import User
from lessinline.business.models import Business, Category


class BusinessTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(title='Medical')
        user = User.objects.create_user(email='admin@example.com', password='12345', first_name='Admin')
        business = Business.objects.create(owner=user, name='LessInLine', category=category, description='Lorem')

        staff_1 = User.objects.create_user(email='staff1@gmail.com', password='12345', first_name='Staff1')
        staff_2 = User.objects.create_user(email='staff2@gmail.com', password='12345', first_name='Staff2')

        business.staffs.add(staff_1)
        business.staffs.add(staff_2)

    def test_business(self):
        b = Business.objects.get(name='LessInLine')
        self.assertEqual(b.description, 'Lorem')

        self.assertIsNotNone(b.staffs.all())
