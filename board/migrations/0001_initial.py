# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('descript', models.TextField(blank=True, default='')),
                ('end', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descript', models.TextField(blank=True, default='')),
                ('status', models.SmallIntegerField(choices=[(1, 'Not Started'), (2, 'In Processing'), (3, 'Testing'), (4, 'Done')], default=1)),
                ('order', models.SmallIntegerField(default=0)),
                ('started', models.DateField(blank=True, null=True)),
                ('due', models.DateField(blank=True, null=True)),
                ('completed', models.DateField(blank=True, null=True)),
                ('sprint', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='board.Sprint')),
            ],
        ),
    ]
