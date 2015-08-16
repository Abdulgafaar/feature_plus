from __future__ import unicode_literals

from unittest2 import TestCase
from ..models import Feature
from ..services import update_other_priorities
from ..factories import FeatureFactory


class FeatureServicesTestCase(TestCase):
    def setUp(self):
        Feature.objects.all().delete()
        self.feature = FeatureFactory.create_batch(3)
        self.feature[0].priority = 1
        self.feature[1].priority = 65
        self.feature[2].priority = 92
        self.feature[0].save(), self.feature[1].save(), self.feature[2].save()

    def test_we_can_update_other_priorities_when_a_new_feature_with_priority_one_is_created(self):
        features_priorities = Feature.objects.all().values_list('priority', flat=True).order_by('priority')
        self.assertListEqual(list(features_priorities), [1, 65, 92])

        new_feature = FeatureFactory.create(priority=1)  # create a new feature with priority 1

        update_other_priorities(new_feature)
        features_priorities = Feature.objects.all().values_list('priority', flat=True).order_by('priority')
        self.assertEqual(list(features_priorities), [1, 2, 66, 93])

    def test_we_can_update_other_priorities_when_an_existing_feature_changes_priority_to_one(self):
        features_priorities = Feature.objects.all().values_list('priority', flat=True).order_by('priority')
        self.assertListEqual(list(features_priorities), [1, 65, 92])

        self.feature[2].priority = 1  # set feature[2] to priority 1
        self.feature[2].save()

        update_other_priorities(self.feature[2])
        features_priorities = Feature.objects.all().values_list('priority', flat=True).order_by('priority')
        self.assertEqual(list(features_priorities), [1, 2, 66])
