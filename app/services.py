from __future__ import unicode_literals, absolute_import

"""
This file contains Business Logic for the `app` Django Application
"""
from django.db.models.expressions import F
from .models import Feature, PRIORITY_ONE

__author__ = 'inspaya'


def update_other_priorities(feature_object):
    """
    Set the priority of this Feature object to 1 and increment all others by 1
    :param feature_object:
    :return:
    """
    if feature_object.priority == PRIORITY_ONE:
        all_features = Feature.objects.all()
        all_features.update(priority=F('priority') + 1)
        feature_object.save()
