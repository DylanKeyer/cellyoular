# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('carrier', models.CharField(max_length=30)),
                ('quote', models.IntegerField()),
                ('condition', models.CharField(max_length=8)),
                ('storage', models.IntegerField()),
            ],
        ),
    ]
