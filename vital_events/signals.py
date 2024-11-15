from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import BirthCertificate


@receiver(post_save, sender=BirthCertificate)
def send_birth_certificate_email(sender, instance, created, **kwargs):
    if created:  # Only send email on creation
        subject = "Birth Certificate Application Received"
        message_text = (
            f"Hello {instance.applicant_name},\n\n"
            f"Thank you for submitting your application for a birth certificate for {instance.first_name} {instance.last_name}.\n"
            f"Your application number is {instance.application_number}.\n\n"
            "We will process your application and notify you of any updates.\n\n"
            "Best regards,\n"
            "eKebele Team"
        )

        # HTML version of the email
        html_message = f"""
        <html>
            <body>
                <p>Dear <strong>{instance.applicant_name}</strong>,</p>
                <p>Thank you for submitting your application for a birth certificate for <strong>{instance.first_name} {instance.last_name}</strong>.</p>
                <p>Your application number is <h3 style="color:green;">{instance.application_number}</h3>.</p>
                <p>We will process your application and notify you of any updates.</p>
                <br>
                <p>Best regards,</p>
                <p><strong>eKebele Team</strong></p>
            </body>
        </html>
        """

        try:
            send_mail(
                subject,
                # Plain text version (fallback for non-HTML email clients)
                message_text,
                "ekebele.eth@gmail.com",  # Sender email
                [instance.applicant_email_address],  # Recipient email
                html_message=html_message  # HTML version
            )
        except Exception as e:
            print(f"Failed to send email: {e}")
        else:
            print("================ Email sent successfully")
