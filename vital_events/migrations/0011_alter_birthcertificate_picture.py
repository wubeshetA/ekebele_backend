# Generated by Django 5.1.2 on 2024-11-18 05:54

import vital_events.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vital_events', '0010_birthcertificate_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthcertificate',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='vital_events/images/', validators=[vital_events.validators.validate_image_size]),
        ),
    ]