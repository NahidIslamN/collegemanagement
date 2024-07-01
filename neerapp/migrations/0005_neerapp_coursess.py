# Generated by Django 5.0.2 on 2024-02-20 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0007_alter_semester_semester_id'),
        ('neerapp', '0004_viceprincipal'),
    ]

    operations = [
        migrations.CreateModel(
            name='neerapp_coursess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dep_Image', models.ImageField(upload_to='course_image')),
                ('dep_description', models.TextField()),
                ('dep_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.departments')),
            ],
        ),
    ]
