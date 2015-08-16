from django.conf.urls import url
from .views import features

urlpatterns = [
    url(r'^features$', features(), name='features_view'),
]
