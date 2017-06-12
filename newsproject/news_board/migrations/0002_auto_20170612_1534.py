# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 06:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsboard',
            name='user_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_info', to='user.UserInfo'),
        ),
    ]
