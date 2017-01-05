# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_delete_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('code', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('carrier', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('condition', models.CharField(max_length=8)),
                ('date_listed', models.CharField(max_length=15)),
                ('storage', models.IntegerField()),
            ],
        ),
    ]
