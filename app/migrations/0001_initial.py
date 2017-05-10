# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('errors_num', models.PositiveIntegerField(default=0)),
                ('statistics', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('analysis_date', models.DateTimeField(verbose_name='last analysis date')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Repository'),
        ),
    ]