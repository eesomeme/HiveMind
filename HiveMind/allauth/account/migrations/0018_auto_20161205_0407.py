# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_remove_notex_hivepk'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='hivepk',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='notex',
            name='hivepk',
            field=models.IntegerField(default=0),
        ),
    ]
