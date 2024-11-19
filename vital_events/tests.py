import logging
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from vital_events.models import BirthCertificate
from vital_events.serializers import BirthCertificateSerializer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

User = get_user_model()


class BirthCertificateTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            phone_number='0912345678',
            first_name='Test',
            last_name='User'
        )
        self.client.login(email='testuser@example.com',
                          password='testpassword')
        logger.info("Setup complete: Test user created and logged in.")

        self.birth_certificate_data = {
            'applicant_name': 'Abebe Kebede',
            'first_name': 'Abebe',
            'middle_name': 'Kebede',
            'last_name': 'Gebremariam',
            'nationality': 'Ethiopian',
            'father_fullname': 'Kebede Gebremariam',
            'father_nationality': 'Ethiopian',
            'mother_fullname': 'Aster Alemu',
            'mother_nationality': 'Ethiopian',
            'dob': '2023-01-01',
            'country_of_birth': 'Ethiopia',
            'region_of_birth': 'Addis Ababa',
            'place_of_birth': 'Bole',
            'gender': 'male',
            'applicant_email_address': 'abebe@example.com',
            'phone_number': '0912345678'
        }

    def test_create_birth_certificate(self):
        # Ensure this matches the URL name in urls.py
        url = reverse('vital-events-list-create')
        logger.info("Sending POST request to create a BirthCertificate with data: %s",
                    self.birth_certificate_data)
        # Force authenticate the client
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            url, self.birth_certificate_data, format='json')
        logger.info("Received response with status code: %d",
                    response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BirthCertificate.objects.count(), 1)
        birth_certificate = BirthCertificate.objects.get()
        self.assertEqual(birth_certificate.applicant_name, 'Abebe Kebede')
        logger.info("BirthCertificate created successfully with application number: %s",
                    birth_certificate.application_number)

    def test_retrieve_birth_certificate(self):
        birth_certificate = BirthCertificate.objects.create(
            user=self.user, **self.birth_certificate_data)
        url = reverse('vital-events-detail', args=[birth_certificate.id])
        logger.info(
            "Sending GET request to retrieve BirthCertificate with ID: %d", birth_certificate.id)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        logger.info("Received response with status code: %d",
                    response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['applicant_name'], 'Abebe Kebede')

    def test_update_birth_certificate(self):
        birth_certificate = BirthCertificate.objects.create(
            user=self.user, **self.birth_certificate_data)
        url = reverse('vital-events-detail', args=[birth_certificate.id])
        updated_data = self.birth_certificate_data.copy()
        updated_data['status'] = 'approved'
        logger.info(
            "Sending PUT request to update BirthCertificate with ID: %d", birth_certificate.id)
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, updated_data, format='json')
        logger.info("Received response with status code: %d",
                    response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        birth_certificate.refresh_from_db()
        self.assertEqual(birth_certificate.status, 'pending')
        logger.info(
            "BirthCertificate updated successfully with new status: %s", birth_certificate.status)

    def test_valid_birth_certificate_serializer(self):
        serializer = BirthCertificateSerializer(
            data=self.birth_certificate_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(
            serializer.validated_data['applicant_name'], 'Abebe Kebede')

    def test_invalid_birth_certificate_serializer(self):
        invalid_data = self.birth_certificate_data.copy()
        invalid_data['applicant_name'] = ''
        serializer = BirthCertificateSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('applicant_name', serializer.errors)

    def test_birth_certificate_serializer_read_only_fields(self):
        birth_certificate = BirthCertificate.objects.create(
            user=self.user, **self.birth_certificate_data)
        serializer = BirthCertificateSerializer(birth_certificate)
        self.assertEqual(
            serializer.data['application_number'], birth_certificate.application_number)
        self.assertEqual(serializer.data['user'], self.user.id)

    def test_application_number_generation(self):
        birth_certificate = BirthCertificate.objects.create(
            user=self.user, **self.birth_certificate_data)
        self.assertIsNotNone(birth_certificate.application_number)
        self.assertEqual(len(birth_certificate.application_number), 7)
        logger.info("Application number generated successfully: %s",
                    birth_certificate.application_number)

    def test_status_change_detection(self):
        birth_certificate = BirthCertificate.objects.create(
            user=self.user, **self.birth_certificate_data)
        birth_certificate.status = 'approved'
        birth_certificate.save()
        self.assertTrue(birth_certificate._status_changed)
        self.assertEqual(birth_certificate._previous_status, 'pending')
        logger.info("Status change detected successfully: from %s to %s",
                    birth_certificate._previous_status, birth_certificate.status)
