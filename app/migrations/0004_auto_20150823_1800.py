# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150818_1839'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='feature',
            unique_together=set([('title', 'clients', 'priority')]),
        ),
    ]
