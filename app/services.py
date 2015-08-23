from __future__ import unicode_literals, absolute_import

"""
This file contains Business Logic for the `app` Django Application
"""
from django.db.models.expressions import F
from .models import Feature, PRIORITY_ONE

__author__ = 'inspaya'


def update_other_priorities(feature, **feature_object_dict):
    """
    Set the priority of this Feature object to 1 and increment all others by 1
    :param feature_object_dict:
    :return:
    """
    if not feature:
        feature = Feature(**feature_object_dict)

    all_features = Feature.objects.all()
    if feature.priority == PRIORITY_ONE:
        # bump every other feature except this one's priority by 1
        all_features.exclude(id=feature.id).update(priority=F('priority') + 1)
    elif feature.priority in all_features.values_list('priority', flat=True):
        # bump every feature greater than or equal to this one by 1
        all_features.filter(priority__gte=feature.priority).update(priority=F('priority') + 1)

    feature.save()
