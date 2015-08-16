from django.conf.urls import url
from .views import features_add, features_list, features_delete

urlpatterns = [
    url(r'^/add$', features_add, name='features_add'),
    url(r'^/list$', features_list, name='features_list'),
    url(r'^/delete$', features_delete, name='features_delete'),
]
