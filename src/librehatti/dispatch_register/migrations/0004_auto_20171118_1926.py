# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch_register', '0003_auto_20171117_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='company',
            new_name='agency',
        ),
    ]
