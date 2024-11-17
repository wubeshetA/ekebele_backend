from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from accounts.models import User


@receiver(post_save, sender=User)
def send_verification_email(sender, instance, created, **kwargs):
    if created:  # Only for newly created users
        # Generate and save verification code
        instance.generate_verification_code()

        # Send email
        send_mail(
            subject="Verify Your Email",
            message=f"Hello {instance.first_name},\n\n"
                    f"Your verification code is: {instance.verification_code}\n\n"
                    f"Please verify your email to activate your account.",
            from_email="eKebele Team <ekebele.eth@gmail.com>",
            recipient_list=[instance.email],
            fail_silently=False,
        )
