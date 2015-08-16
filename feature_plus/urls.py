from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^features', include('app.urls'), name='features_app'),
]
