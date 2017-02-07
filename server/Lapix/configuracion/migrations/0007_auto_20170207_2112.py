# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0006_auto_20170131_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='configuracionperiodo',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='ano',
            field=models.IntegerField(choices=[(2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024')], default=2017),
        ),
    ]
