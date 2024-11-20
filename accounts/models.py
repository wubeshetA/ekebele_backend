# accounts/models.py


from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.db import models
import random
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

    username = None  # We are not using the username field
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    nid = models.CharField(max_length=12, unique=True, blank=True, null=True)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

    # Default to inactive until verified
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def generate_verification_code(self):
        """Generate a random 6-digit verification code."""
        self.verification_code = str(random.randint(100000, 999999))
        self.save()
