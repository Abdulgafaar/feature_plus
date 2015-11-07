from __future__ import unicode_literals, absolute_import

from .base import *

DEBUG = True
INSTALLED_APPS += (
    'lettuce.django',
    'debug_toolbar',
    'django_coverage',
)

LETTUCE_APPS = (
    'app',
)
