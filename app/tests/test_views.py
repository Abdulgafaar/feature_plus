from __future__ import unicode_literals, absolute_import

from unittest2 import TestCase

from django.test import Client, RequestFactory
from django.core.urlresolvers import reverse
from ..models import Feature
from ..views import add_edit_feature, list_features
from ..factories import FeatureFactory


class FeatureViewsTestCase(TestCase):
    def setUp(self):
        Feature.objects.all().delete()
        self.feature = FeatureFactory.build(target_date='2015-11-23')
        self.request = RequestFactory()
        self.client = Client(enforce_csrf_checks=True)

    def test_we_can_list_all_features_with_correct_count(self):
        FeatureFactory.create_batch(3)
        response = self.client.get(reverse('features:list_features'))
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.resolver_match.func, list_features)
        self.assertEqual(response.context['list_of_features'].count(), 3)

    def test_we_can_post_a_new_feature(self):
        request = self.request.post(reverse('features:add_edit_feature'), data=self.feature.__dict__)
        response = add_edit_feature(request)
        self.assertTrue(Feature.objects.filter(title=self.feature.title).exists())
        self.assertEqual(302, response.status_code)

    def test_we_can_update_an_existing_feature(self):
        new_feature = FeatureFactory.create(target_date='2015-01-03')
        request = self.request.post(reverse('features:add_edit_feature'), data=new_feature.__dict__)
        response = add_edit_feature(request, new_feature.id)
        self.assertTrue(Feature.objects.filter(title=new_feature.title).exists())
        self.assertEqual(302, response.status_code)
