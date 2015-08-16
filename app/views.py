from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

from .forms import FeatureForm
from .models import Feature


@csrf_protect
def features_add(request):
    """
    Add/Edit Feature
    :param request:
    :return:
    """
    if request.method == 'POST':
        feature_form = FeatureForm(request.POST)
        if feature_form.is_valid():
            HttpResponseRedirect('/list')
    else:
        feature_form = FeatureForm()

    return render_to_response('features.html', {'feature_form': feature_form})


def features_list(request):
    """
    Return List of available features
    :param request:
    :return:
    """
    template = loader.get_template('features.html')
    return HttpResponse(template.render({}))


def features_delete(request):
    """
    Return List of available features
    :param request:
    :return:
    """

    return HttpResponse({})
