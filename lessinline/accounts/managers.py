from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email: str, first_name: str, password: str = None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        if not first_name:
            raise ValueError('User must have a name')

        # Create user with given email and password
        user = self.model(email=self.normalize_email(email), first_name=first_name, **extra_fields)

        if password:
            user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, first_name: str, password: str = None, **extra_fields):
        user = self.create_user(email, first_name, password, **extra_fields)

        # Every admin is a staff
        user.is_admin = True

        user.save(using=self._db)
        return user


class ActiveUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
