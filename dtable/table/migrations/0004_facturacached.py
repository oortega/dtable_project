# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-11-12 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_auto_20201031_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaCached',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('data', models.TextField(blank=True)),
            ],
        ),
    ]
