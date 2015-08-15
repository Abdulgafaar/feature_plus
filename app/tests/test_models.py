from __future__ import unicode_literals

from unittest2 import TestCase
from ..factories import FeatureFactory


class FeatureTestCase(TestCase):
    """
    Test Feature model
    """

    def test_unicode_is_correctly_returned(self):
        feature = FeatureFactory(title='Draggable masthead')
        self.assertEqual(unicode(feature), "{}".format(feature.title))
