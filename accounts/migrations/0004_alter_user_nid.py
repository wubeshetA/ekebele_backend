# Generated by Django 5.1.2 on 2024-11-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_nid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nid',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]
