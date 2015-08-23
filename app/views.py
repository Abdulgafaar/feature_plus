from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, RequestContext

from .forms import FeatureForm
from .models import Feature
from .services import update_other_priorities


def add_edit_feature(request, id=None):
    """
    Add/Edit Feature
    :param request:
    :return:
    """
    feature = None
    if request.method == 'POST':
        feature = Feature.objects.filter(title=request.POST['title']).first()
        feature_form = FeatureForm(request.POST, instance=feature)
        if feature_form.is_valid():
            update_other_priorities(feature, **feature_form.cleaned_data)
            return HttpResponseRedirect(reverse('features:list_features'))
    else:
        if id:
            feature = Feature.objects.filter(id=int(id)).first()

        feature_form = FeatureForm(instance=feature)

    return render_to_response('add_edit_features.html',
                              {'feature_form': feature_form},
                              RequestContext(request)
                              )


def list_features(request):
    """
    Return List of available features
    :param request:
    :return:
    """
    features = Feature.objects.all()
    template = loader.get_template('list_features.html')
    context = RequestContext(request, {'list_of_features': features})
    return HttpResponse(template.render(context))


def delete_feature(request, id):
    """
    Deletes a feature from the DB
    :param request:
    :param id:
    :return:
    """
    try:
        Feature.objects.get(id=int(id)).delete()
    except Feature.DoesNotExist:
        return render_to_response('404.html', {'not_found': "Feature not found."})

    return HttpResponseRedirect(reverse('features:list_features'))
