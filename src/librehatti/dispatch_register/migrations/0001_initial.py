# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='entry',
            fields=[
                ('dispatch_no', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name_of_Dept_or_Client', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('agency', models.CharField(max_length=200, blank=True)),
                ('subject', models.CharField(max_length=200)),
                ('remarks', models.CharField(max_length=200)),
                ('choices', models.ForeignKey(to='dispatch_register.Choices')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
