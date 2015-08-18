from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, RequestContext

from .forms import FeatureForm


def features_add(request):
    """
    Add/Edit Feature
    :param request:
    :return:
    """
    if request.method == 'POST':
        feature_form = FeatureForm(request.POST)
        if feature_form.is_valid():
            feature_form.save()
            return HttpResponseRedirect(reverse('features_list'))
    else:
        feature_form = FeatureForm()

    return render_to_response('features.html',
                              {'feature_form': feature_form},
                              RequestContext(request)
                              )


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
