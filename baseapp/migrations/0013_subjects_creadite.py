# Generated by Django 5.0.3 on 2024-03-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0012_attendanceobject_shift_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='Creadite',
            field=models.IntegerField(default=0),
        ),
    ]
