# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('state', models.CharField(max_length=100, verbose_name='State')),
                ('id_json', models.CharField(max_length=100, verbose_name='Id')),
                ('purpose', models.CharField(max_length=50, verbose_name='Purpose')),
                ('listing_type', models.CharField(max_length=50, verbose_name='Listing Type')),
                ('published_on', models.CharField(max_length=50, verbose_name='Published On')),
            ],
            options={
                'verbose_name_plural': 'Imoveis',
            },
        ),
    ]
