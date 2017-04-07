# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yahoo_id', models.CharField(max_length=1000)),
                ('chinese_name', models.CharField(max_length=1000)),
                ('english_name', models.CharField(max_length=1000)),
                ('yahoo_poster', models.CharField(max_length=1000)),
                ('yahoo_movie_link', models.CharField(max_length=1000)),
                ('yahoo_trailer', models.CharField(max_length=1000)),
                ('yahoo_release_data', models.CharField(max_length=1000)),
                ('yahoo_category', models.CharField(max_length=1000)),
                ('yahoo_length', models.CharField(max_length=1000)),
                ('yahoo_director', models.CharField(max_length=1000)),
                ('yahoo_actor', models.CharField(max_length=1000)),
                ('yahoo_company', models.CharField(max_length=1000)),
                ('yahoo_official_website', models.CharField(max_length=1000)),
                ('yahoo_description', models.CharField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='MovieQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]