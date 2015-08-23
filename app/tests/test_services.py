from __future__ import unicode_literals, absolute_import

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

    def test_that_creating_a_feature_with_an_existing_priority_bumps_other_features_with_same_or_higher_priorities(
            self):
        features_priorities = Feature.objects.all().values_list('priority', flat=True).order_by('priority')
        self.assertListEqual(list(features_priorities), [1, 65, 92])

        # create a new feature with priority 92 and note that self.feature[2] is currently 92
        new_feature = FeatureFactory.create(priority=92)

        update_other_priorities(new_feature)
        features_priorities = Feature.objects.all().values_list('priority', flat=True).order_by('priority')
        self.assertEqual(list(features_priorities), [1, 65, 92, 93])

    def test_that_updating_a_feature_with_an_existing_priority_bumps_other_features_with_same_or_higher_priorities(
            self):
        features_priorities = Feature.objects.all().values_list('priority', flat=True).order_by('priority')
        self.assertListEqual(list(features_priorities), [1, 65, 92])

        self.feature[1].priority = 92  # note that self.feature[2] is currently 92
        self.feature[1].save()

        update_other_priorities(self.feature[1])
        features_priorities = Feature.objects.all().values_list('priority', flat=True).order_by('priority')
        self.assertEqual(list(features_priorities), [1, 92, 93])

    def test_that_creating_two_new_features_and_updating_an_existing_feature_with_successive_priorities(self):
        features_priorities = Feature.objects.all().values_list('priority', flat=True).order_by('priority')
        self.assertListEqual(list(features_priorities), [1, 65, 92])

        # create a new feature with priority 67
        new_feature1 = FeatureFactory.create(priority=67)
        update_other_priorities(new_feature1)

        # change an existing feature to priority 66
        self.feature[1].priority = 66
        self.feature[1].save()
        update_other_priorities(self.feature[1])

        # create a new feature with priority 66
        new_feature2 = FeatureFactory.create(priority=66)
        update_other_priorities(new_feature2)

        features_priorities = Feature.objects.all().values_list('priority', flat=True).order_by('priority')
        self.assertEqual(list(features_priorities), [1, 66, 67, 69, 95])
