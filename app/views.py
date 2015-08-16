from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import RequestContext, loader


def features(request):
    """
    Handles CRUD operations for the Bootstrap template
    :param request:
    :return:
    """
    template = loader.get_template('features.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
