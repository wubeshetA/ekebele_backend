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


@receiver(post_save, sender=BirthCertificate)
def notify_status_change(sender, instance, created, **kwargs):
    # Only send notification if the status has changed
    if not created and hasattr(instance, '_status_changed') and instance._status_changed:
        if instance._previous_status == 'pending':
            # Handle approved status
            if instance.status == 'approved':
                if instance.applicant_email_address:
                    send_mail(
                        subject="Birth Certificate Approved",
                        message=f"Dear {instance.first_name} {instance.last_name},\n\n"
                                "Your birth certificate application has been approved. "
                                "You can view and download your certificate on eKebele portal.\n\n"
                                "Thank you,\nThe eKebele Team",
                        from_email="eKebele Team <ekebele.eth@gmail.com>",
                        recipient_list=[instance.applicant_email_address],
                        fail_silently=False,
                    )

            # Handle rejected status
            elif instance.status == 'rejected':
                if instance.applicant_email_address:
                    send_mail(
                        subject="Birth Certificate Application Status",
                        message=f"Dear {instance.first_name} {instance.last_name},\n\n"
                                f"We regret to inform you that your birth certificate application has been rejected. \n"
                                f"Reason: {instance.comment if instance.comment else 'Not specified'}.\n\n"
                                "Please contact our support team for more information.\n\n"
                                "Thank you,\nThe eKebele Team",
                        from_email="eKebele Team <ekebele.eth@gmail.com>",
                        recipient_list=[instance.applicant_email_address],
                        fail_silently=False,
                    )
