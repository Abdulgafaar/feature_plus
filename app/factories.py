from __future__ import unicode_literals

from datetime import datetime
from pytz import UTC
from factory.fuzzy import BaseFuzzyAttribute, FuzzyText, FuzzyChoice, FuzzyInteger, FuzzyDateTime
from factory.django import DjangoModelFactory
from .models import Feature


class FuzzyURL(BaseFuzzyAttribute):
    """
    Generates random urls
    """

    def fuzz(self):
        return "http://{domain}{tld}".format(domain=FuzzyText().fuzz(),
                                             tld=FuzzyChoice(['.com', '.net', '.org']).fuzz())


class FeatureFactory(DjangoModelFactory):
    """
    Creates dynamic fixtures for the Feature Object
    """

    class Meta:
        model = Feature

    title = FuzzyText(length=100)
    description = FuzzyText(length=255)
    clients = FuzzyChoice(['Client A', 'Client B', 'Client C'])
    priority = FuzzyInteger(1, 100, 1)
    target_date = FuzzyDateTime(datetime(2015, 8, 15, tzinfo=UTC))
    ticket_url = FuzzyURL()
    product_area = FuzzyChoice(['Policies', 'Billing', 'Claims', 'Reports'])
