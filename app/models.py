from __future__ import unicode_literals

from django.db import models

CLIENTS = (
    ('Client A', 'Client A'),
    ('Client B', 'Client B'),
    ('Client C', 'Client C'),
)

PRODUCT_AREAS = (
    ('Policies', 'Policies'),
    ('Billing', 'Billing'),
    ('Claims', 'Claims'),
    ('Reports', 'Reports'),
)


class Feature(models.Model):
    """
    Represents a Feature object.
    """
    title = models.CharField(max_length=100, help_text='Title')
    description = models.TextField(help_text='Description')
    clients = models.CharField(max_length=35, choices=CLIENTS, help_text='Client')
    priority = models.IntegerField(help_text='Client Priority')
    target_date = models.DateTimeField(help_text='Date Expected')
    ticket_url = models.URLField(help_text='Ticket URL')
    product_area = models.CharField(max_length=35, choices=PRODUCT_AREAS, help_text='Product Area')

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __unicode__(self):
        return self.title
