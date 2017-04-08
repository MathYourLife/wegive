# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-26 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wegiveapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=16)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='charity',
            name='tags_csv',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='donor',
            name='tags_csv',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='donation',
            name='charity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wegiveapp.Charity'),
        ),
        migrations.AddField(
            model_name='donation',
            name='donor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wegiveapp.Donor'),
        ),
    ]
