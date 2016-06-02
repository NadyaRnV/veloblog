# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(verbose_name='Дата публикации')),
                ('content', models.TextField(max_length=10000)),
            ],
        ),
    ]
