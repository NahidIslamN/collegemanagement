# Generated by Django 5.0.2 on 2024-03-11 04:53

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0020_alter_semester_semester_id_message_model_for_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
                ('Security_key', models.CharField(max_length=250)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('location', models.CharField(max_length=100)),
                ('established_date', models.DateField(default=django.utils.timezone.now)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavingsAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=10, unique=True)),
                ('Security_key', models.CharField(max_length=250)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseapp.main_bank')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
