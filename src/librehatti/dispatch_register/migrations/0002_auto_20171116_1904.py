# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('remarks', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='dispatch_register',
        ),
    ]
