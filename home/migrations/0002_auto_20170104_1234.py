# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='id',
        ),
        migrations.AddField(
            model_name='phone',
            name='code',
            field=models.CharField(default='XXX000', max_length=10, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
