# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='title',
            field=models.CharField(help_text='Title', unique=True, max_length=100),
        ),
    ]
