# Generated by Django 5.0.1 on 2024-02-01 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0003_remove_teacher_sub_id_teacher_sub_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='Dep_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.departments'),
        ),
    ]
