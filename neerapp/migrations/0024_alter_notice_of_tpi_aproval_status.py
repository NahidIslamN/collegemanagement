# Generated by Django 5.0.2 on 2024-03-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neerapp', '0023_alter_notice_of_tpi_expird_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice_of_tpi',
            name='aproval_status',
            field=models.CharField(default='1', max_length=1),
        ),
    ]
