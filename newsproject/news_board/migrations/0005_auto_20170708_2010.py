# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-08 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_board', '0004_auto_20170624_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsboard',
            name='mode',
            field=models.IntegerField(choices=[(1, '공지사항'), (2, '자유게시판'), (3, '비트코인')]),
        ),
    ]
