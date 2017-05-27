# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-24 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ukpython', '0002_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='user_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='ukpython.UserGroup'),
        ),
    ]