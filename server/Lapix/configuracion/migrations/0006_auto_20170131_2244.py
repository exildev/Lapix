# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-31 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0005_merge_20170131_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.Sede'),
        ),
    ]
