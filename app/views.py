from django import form
from django.shortcuts import render
from .models import Feature


class FeatureForm(form.ModelForms):
  """
  Form for creating new Feature entry
  """
  class Meta:
    model = Feature
  
