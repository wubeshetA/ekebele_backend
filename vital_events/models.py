from django.db import models
import random

# Create your models here.

from django.db import models


class BirthCertificate(models.Model):

    # APPLICANT_RELATIONSHIP_CHOICES = [

    #     ('parent', 'Parent'),
    #     ('guardian', 'Guardian'),
    #     ('other', 'Other'),

    # ]

    APPLICATION_STATUS_CHOICES = [

        ('pending', 'Pending'),

        ('approved', 'Approved'),

        ('rejected', 'Rejected'),

    ]

    applicant_name = models.CharField(max_length=255)

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)

    father_fullname = models.CharField(max_length=255)
    father_nationality = models.CharField(max_length=255)

    mother_fullname = models.CharField(max_length=255)
    mother_nationality = models.CharField(max_length=255)

    dob = models.DateField(verbose_name="Date of Birth")

    country_of_birth = models.CharField(max_length=255)
    region_of_birth = models.CharField(max_length=255)
    place_of_birth = models.CharField(max_length=255)

    gender = models.CharField(max_length=10, choices=[
                              ('male', 'Male'), ('female', 'Female')])

    applicant_email_address = models.EmailField(
        blank=True, null=True)  # Not mandatory

    phone_number = models.CharField(max_length=15)
    application_number = models.CharField(
        max_length=7, unique=True, editable=False)
    status = models.CharField(
        max_length=10, choices=APPLICATION_STATUS_CHOICES, default='pending')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    comment = models.TextField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.application_number:
            self.application_number = str(random.randint(1000000, 9999999))
        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.child_name} - {self.applicant_name}"
