from django.db.models.signals import post_save
from django.dispatch import receiver
from mailersend.emails import NewEmail
from .models import BirthCertificate

api_key = 'mlsn.c7eb179e017db3351736fd4dbe14508a115c5fdcc03eaa009ffb4cf99ffe0f80'
mailer = NewEmail(api_key)


@receiver(post_save, sender=BirthCertificate)
def send_birth_certificate_email(sender, instance, created, **kwargs):
    print("==============Signal received======")
    # if created and instance.applicant_email_address:

    #     subject = "Your Birth Certificate Application"
    #     message_text = (
    #         f"Hello {instance.applicant_name},\n\n"
    #         f"Thank you for submitting your application for a birth certificate for {instance.child_name}.\n"
    #         f"Your application number is {instance.application_number}.\n\n"
    #         "We will process your application and notify you of any updates.\n\n"
    #         "Best regards,\n"
    #         "eKebele Team"
    #     )
        
    #     message_html = "<p>" + message_text.replace("\n", "<br>") + "</p>"

    #     mail_from = {
    #         "name": "eKebele Team",
    #         "email": "wubeane@gmail.com"
    #     }
    #     recipients = [{"name": instance.applicant_name,
    #                    "email": instance.applicant_email_address}]

    #     mail_body = {}
    #     mailer.set_mail_from(mail_from, mail_body)
    #     mailer.set_mail_to(recipients, mail_body)
    #     mailer.set_subject(subject, mail_body)
    #     mailer.set_plaintext_content(message_text, mail_body)
    #     mailer.set_html_content(message_html, mail_body)

    #     try:
    #         mailer.send(mail_body)
    #     except Exception as e:
    #         print("Error sending email: ", e)
    #     else:
    #         print("Email sent successfully")
