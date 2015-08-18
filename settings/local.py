from __future__ import unicode_literals, absolute_import

from .base import *

DEBUG = True
INSTALLED_APPS += (
    'lettuce.django',
)

LETTUCE_APPS = (
    'app',
)
