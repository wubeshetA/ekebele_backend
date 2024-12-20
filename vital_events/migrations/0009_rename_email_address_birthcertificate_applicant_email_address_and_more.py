# Generated by Django 5.1.2 on 2024-11-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vital_events', '0008_birthcertificate_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='birthcertificate',
            old_name='email_address',
            new_name='applicant_email_address',
        ),
        migrations.RenameField(
            model_name='birthcertificate',
            old_name='child_name',
            new_name='country_of_birth',
        ),
        migrations.RemoveField(
            model_name='birthcertificate',
            name='relationship_to_child',
        ),
        migrations.AddField(
            model_name='birthcertificate',
            name='father_fullname',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='birthcertificate',
            name='father_nationality',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='birthcertificate',
            name='first_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='birthcertificate',
            name='last_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='birthcertificate',
            name='middle_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='birthcertificate',
            name='mother_fullname',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='birthcertificate',
            name='mother_nationality',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='birthcertificate',
            name='nationality',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='birthcertificate',
            name='region_of_birth',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
