# Generated by Django 5.0.2 on 2024-03-11 04:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neerapp', '0022_public_masseges_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice_of_tpi',
            name='Expird_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
