# Generated by Django 5.1.2 on 2024-11-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vital_events', '0009_rename_email_address_birthcertificate_applicant_email_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthcertificate',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='vital_events/images/'),
        ),
    ]
