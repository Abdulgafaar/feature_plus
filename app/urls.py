from django.conf.urls import url
from .views import add_edit_feature, list_features, delete_feature

urlpatterns = [
    url(r'^/$', add_edit_feature, name='add_edit_feature'),
    url(r'^/list/$', list_features, name='list_features'),
    url(r'^/edit/(?P<id>[\d]+)/$', add_edit_feature, name='edit_feature'),
    url(r'^/delete/(?P<id>[\d]+)/$', delete_feature, name='delete_feature'),
]
