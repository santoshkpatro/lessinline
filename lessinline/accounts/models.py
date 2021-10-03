import uuid
import shortuuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager, ActiveUserManager


class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=8, blank=True, null=True, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    password_reset_required = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()
    active_users = ActiveUserManager()

    class Meta:
        db_table = 'users'
        ordering = ['email']

    def __str__(self) -> str:
        return self.email

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self) -> str:
        # Return the first_name plus the last_name, with a space in between.
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self) -> str:
        # Return the short name for the user.
        return self.first_name

    # Admin Panel permissions
    def has_perm(self, perm, obj=None) -> bool:
        # Does the user have a specific permission?
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label) -> bool:
        # Does the user have permissions to view the app `app_label`?
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # Is the user a member of staff?
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_number = models.CharField(max_length=12, blank=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    balance = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts'

    def __str__(self) -> str:
        return self.account_number

    def save(self, *args, **kwargs) -> None:
        if not self.account_number:
            self.account_number = shortuuid.ShortUUID().random(length=10).upper()
        return super().save(*args, **kwargs)
