# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20151225_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='user_location',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
