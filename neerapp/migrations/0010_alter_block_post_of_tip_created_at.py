# Generated by Django 5.0.2 on 2024-02-24 02:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neerapp', '0009_block_post_of_tip_comments_on_block_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block_post_of_tip',
            name='Created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
