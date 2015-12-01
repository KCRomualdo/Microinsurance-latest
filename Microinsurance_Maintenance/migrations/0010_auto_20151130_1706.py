# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Microinsurance_Maintenance', '0009_auto_20151130_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avail',
            name='date_avail',
            field=models.DateField(verbose_name=' *  Date availed:', default=datetime.datetime.now),
        ),
    ]
