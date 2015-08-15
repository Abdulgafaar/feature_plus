# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Title', max_length=100)),
                ('description', models.TextField(help_text=b'Description')),
                ('clients', models.CharField(help_text=b'Client', max_length=35, choices=[(b'Client A', b'Client A'), (b'Client B', b'Client B'), (b'Client C', b'Client C')])),
                ('priority', models.IntegerField(help_text=b'Client Priority')),
                ('target_date', models.DateTimeField(help_text=b'Date Expected')),
                ('ticket_url', models.URLField(help_text=b'Ticket URL')),
                ('product_area', models.CharField(help_text=b'Product Area', max_length=35, choices=[(b'Policies', b'Policies'), (b'Billing', b'Billing'), (b'Claims', b'Claims'), (b'Reports', b'Reports')])),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
    ]
