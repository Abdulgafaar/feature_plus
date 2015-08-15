from __future__ import unicode_literals

from django import forms
from .models import Feature


class FeatureForm(forms.ModelForm):
    """
    Form for creating new Feature entry
    """

    class Meta:
        model = Feature
