# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maptracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='cantidad',
            field=models.IntegerField(),
        ),
    ]