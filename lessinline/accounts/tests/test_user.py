from django.test import TestCase
from django.contrib.auth import authenticate
from lessinline.accounts.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(email='example@gmail.com', first_name='example', password='12345')
        User.objects.create_superuser(email='example2@gmail.com', first_name='example2', password='12345')

    def test_user_created(self):
        user1 = User.objects.get(email='example@gmail.com')
        user2 = User.objects.get(email='example2@gmail.com')

        self.assertEqual(user1.first_name, 'example')
        self.assertEqual(user2.first_name, 'example2')

    def test_user_permissions(self):
        user1 = User.objects.get(email='example@gmail.com')
        user2 = User.objects.get(email='example2@gmail.com')

        self.assertEqual(user1.is_admin, False)
        self.assertEqual(user2.is_admin, True)

    def test_user_password(self):
        user1 = authenticate(email='example@gmail.com', password='12345')
        user2 = authenticate(email='example2@gmail.com', password='12345')

        self.assertIsNotNone(user1)
        self.assertIsNotNone(user2)
