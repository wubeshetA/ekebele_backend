from django.test import TestCase

# Create your tests here.
import logging
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from accounts.backends import PhoneOrEmailBackend
from accounts.models import User
from accounts.serializers import VerifyEmailSerializer, UserProfileSerializer
from django.core import mail

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

User = get_user_model()


class AccountsTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            phone_number='0912345678',
            first_name='Test',
            last_name='User',
            is_active=True  # Set to active for testing purposes
        )
        self.client.login(email='testuser@example.com',
                          password='testpassword')
        logger.info("Setup complete: Test user created and logged in.")

    def test_check_is_staff(self):
        url = reverse('check-is-staff')
        logger.info("Sending GET request to check if user is staff.")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        logger.info("Received response with status code: %d",
                    response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['is_staff'], self.user.is_staff)

    def test_verify_email(self):
        user = User.objects.create_user(
            email='verifyuser@example.com',
            password='testpassword',
            phone_number='0912345679',
            first_name='Verify',
            last_name='User',
            is_active=False
        )
        user.generate_verification_code()
        url = reverse('verify-email')
        data = {
            'email': user.email,
            'verification_code': user.verification_code
        }
        logger.info("Sending POST request to verify email with data: %s", data)
        response = self.client.post(url, data, format='json')
        logger.info("Received response with status code: %d",
                    response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user.refresh_from_db()
        self.assertTrue(user.is_active)
        self.assertIsNone(user.verification_code)

    def test_user_profile_view(self):
        url = reverse('user-profile')
        logger.info("Sending GET request to retrieve user profile.")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        logger.info("Received response with status code: %d",
                    response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    def test_phone_or_email_backend(self):
        backend = PhoneOrEmailBackend()
        user = backend.authenticate(
            request=None, username='testuser@example.com', password='testpassword')
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'testuser@example.com')

        user = backend.authenticate(
            request=None, username='0912345678', password='testpassword')
        self.assertIsNotNone(user)
        self.assertEqual(user.phone_number, '0912345678')

    def test_send_verification_email_signal(self):
        # Clear the mail outbox before the test
        mail.outbox = []

        user = User.objects.create_user(
            email='signaluser@example.com',
            password='testpassword',
            phone_number='0912345680',
            first_name='Signal',
            last_name='User',
            is_active=False
        )

        # Print the contents of the mail outbox for debugging
        for email in mail.outbox:
            logger.info("Email subject: %s", email.subject)
            logger.info("Email recipients: %s", email.to)
            logger.info("Email body: %s", email.body)

        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Verify Your Email', mail.outbox[0].subject)
        self.assertIn(user.email, mail.outbox[0].to)
        self.assertIn(user.verification_code, mail.outbox[0].body)
