from __future__ import unicode_literals, absolute_import

from datetime import datetime
from unittest2 import TestCase
from ..factories import FeatureFactory
from ..forms import FeatureForm


class FeatureFormTestCase(TestCase):
    """
    Test Feature Form
    """

    def setUp(self):
        self.form = FeatureForm

    def test_dates_are_properly_formatted(self):
        feature_data = FeatureFactory.build(target_date="2013-01-01")
        feature_form = self.form(data=feature_data.__dict__)
        self.assertTrue(feature_form.is_valid())  # creates the `cleaned_data` property on feature_form
        cleaned_target_date = feature_form.cleaned_data['target_date']
        raw_date = feature_data.target_date.split('-')
        expected_value = datetime.strftime(datetime(int(raw_date[0]), int(raw_date[1]), int(raw_date[2])),
                                           '%Y-%m-%dT%H:%MZ')
        self.assertEqual(cleaned_target_date, expected_value)
