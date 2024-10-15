from django.db import models


# Create your models here.

from django.db import models


class BirthCertificate(models.Model):

    APPLICANT_RELATIONSHIP_CHOICES = [

        ('parent', 'Parent'),

        ('guardian', 'Guardian'),

        ('other', 'Other'),

    ]

    applicant_name = models.CharField(max_length=255)

    child_name = models.CharField(max_length=255)

    dob = models.DateField(verbose_name="Date of Birth")

    place_of_birth = models.CharField(max_length=255)

    gender = models.CharField(max_length=10, choices=[
                              ('male', 'Male'), ('female', 'Female')])

    relationship_to_child = models.CharField(
        max_length=50, choices=APPLICANT_RELATIONSHIP_CHOICES)

    email_address = models.EmailField(blank=True, null=True)  # Not mandatory

    phone_number = models.CharField(max_length=15)

    def __str__(self):

        return f"{self.child_name} - {self.applicant_name}"
