from django.contrib import admin
from .models import Feature, PRIORITY_ONE
from .services import update_other_priorities


class FeatureAdmin(admin.ModelAdmin):
    model = Feature

    def save_model(self, request, obj, form, change):
        update_other_priorities(obj, **form.cleaned_data)
        super(FeatureAdmin, self).save_model(request, obj, form, change)

admin.site.register(Feature, FeatureAdmin)
