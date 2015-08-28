from __future__ import unicode_literals, absolute_import

from unittest2 import TestCase
from ..factories import FeatureFactory
from ..models import Feature


class FeatureModelTestCase(TestCase):
    """
    Test Feature model
    """

    def setUp(self):
        Feature.objects.all().delete()

    def test_unicode_is_correctly_returned(self):
        feature = FeatureFactory(title='Draggable masthead')
        self.assertEqual(unicode(feature), "{}".format(feature.title))

    def test_uniqueness_is_enforced_when_creating_models(self):
        feature1 = FeatureFactory.create(title='A', clients='Client B', priority=1)
        self.assertTrue(
            Feature.objects.filter(title=feature1.title, clients=feature1.clients, priority=feature1.priority).exists())
        self.assertRaises(Exception, FeatureFactory.create(), title='A', clients='Client B', priority=1)
