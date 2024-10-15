# accounts/backends.py

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.db.models import Q
User = get_user_model()

class PhoneOrEmailBackend(BaseBackend):
    """
    Custom authentication backend to allow login using either
    phone number or email and password.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        try:
            # Try to get user by email or phone number using Q lookup
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try :
                user = User.objects.get(phone_number=username)
            except User.DoesNotExist:
                return None

        # Check if the password is valid
        if user and user.check_password(password):
            return user

        return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None