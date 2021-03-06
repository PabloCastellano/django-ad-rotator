# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-13 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('end_date', models.DateField(verbose_name='End date')),
                ('image', models.ImageField(upload_to='banners', verbose_name='Image')),
                ('link_url', models.URLField(max_length=256, verbose_name='Link URL')),
                ('link_alt_text', models.CharField(max_length=64, verbose_name='Link alt text')),
            ],
            options={
                'ordering': ('start_date',),
            },
        ),
    ]
