# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0002_auto_20160425_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eggcollection',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
