# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 21:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20151218_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachfile', models.CharField(max_length=254, null=True)),
                ('filename', models.CharField(max_length=254)),
                ('filesize', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterModelOptions(
            name='mail',
            options={'ordering': ('-timestamp',)},
        ),
        migrations.AddField(
            model_name='mail',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 21, 48, 33, 169240)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mail',
            name='updatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 21, 48, 43, 103592)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mail',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='attachfile',
            name='mail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Mail'),
        ),
    ]
