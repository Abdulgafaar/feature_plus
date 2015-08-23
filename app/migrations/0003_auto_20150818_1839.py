# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150816_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='priority',
            field=models.PositiveIntegerField(help_text='Client Priority'),
        ),
    ]
