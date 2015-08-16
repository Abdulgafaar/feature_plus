from django.contrib import admin
from .models import Feature, PRIORITY_ONE
from .services import update_other_priorities


class FeatureAdmin(admin.ModelAdmin):
    model = Feature

    def save_model(self, request, obj, form, change):
        if obj.priority == PRIORITY_ONE:
            update_other_priorities(obj)
            super(FeatureAdmin, self).save_model(request, obj, form, change)


admin.site.register(Feature, FeatureAdmin)
