# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-17 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion', '0007_auto_20171217_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companie_name', models.CharField(max_length=250)),
                ('nbEmployee', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('companies_logo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=250)),
                ('employee_surname', models.CharField(max_length=250)),
                ('is_favorite', models.BooleanField(default=False)),
                ('companie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Companie')),
            ],
        ),
    ]
