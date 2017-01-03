# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-03 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('carrier', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('condition', models.CharField(max_length=8)),
                ('date_listed', models.CharField(max_length=15)),
                ('storage', models.IntegerField()),
            ],
        ),
    ]
