from __future__ import unicode_literals

from django import forms
from .models import Feature
from .services import update_other_priorities

__author__ = 'inspaya'


class FeatureForm(forms.ModelForm):
    """
    Custom Data Entry Form
    """

    class Meta:
        model = Feature
        fields = '__all__'

    def clean(self):
        update_other_priorities(self.instance)
        super(FeatureForm, self).clean()
