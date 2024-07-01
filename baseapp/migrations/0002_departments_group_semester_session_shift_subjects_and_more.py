# Generated by Django 5.0.1 on 2024-02-01 13:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dep_ID', models.CharField(max_length=8)),
                ('Dep_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Group_ID', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semester_ID', models.CharField(choices=[(1, 'First Semester'), (2, 'Second Semester'), (3, 'Third Semester'), (4, 'Fourth Semester'), (5, 'Fifth Semester'), (6, 'Sixth Semester'), (7, 'Seventh Semester'), (8, 'Eighth Semester')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Session_Start', models.CharField(max_length=25)),
                ('Session_End', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shift_ID', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub_ID', models.CharField(max_length=8)),
                ('Subjects_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Head_Of_Dep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mobile', models.CharField(max_length=30)),
                ('Gender', models.CharField(max_length=30)),
                ('Date_of_Birth', models.DateField()),
                ('Join_date', models.DateField()),
                ('Dep_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.departments')),
                ('admin', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(max_length=30)),
                ('Join_date', models.DateField()),
                ('Date_of_Birth', models.DateField()),
                ('Mobile', models.CharField(max_length=30)),
                ('Qualification', models.CharField(max_length=50)),
                ('Exprience', models.TextField()),
                ('Address', models.TextField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('District', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('Dep_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.departments')),
                ('Shift_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.shift')),
                ('Sub_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.subjects')),
                ('admin', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
