from django.contrib import admin
from .models import Feature


class FeatureAdmin(admin.ModelAdmin):
    model = Feature


admin.site.register(Feature, FeatureAdmin)
