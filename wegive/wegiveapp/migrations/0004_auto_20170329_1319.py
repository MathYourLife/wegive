# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-29 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wegiveapp', '0003_auto_20170329_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='tags_csv',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='donor',
            name='tags_csv',
            field=models.TextField(blank=True, default=''),
        ),
    ]
