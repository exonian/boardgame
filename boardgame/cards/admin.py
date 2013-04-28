from django.contrib import admin

from . import models


class ModifierOptions(admin.ModelAdmin):
    fields = (
        (
            'component_type',
            'component_id'
        ),
        'operator',
        'magnitude',
        'attribute'
    )
    related_lookup_fields = {
        'generic': [['component_type', 'component_id']],
    }


admin.site.register(models.Modifier, ModifierOptions)
admin.site.register(models.Trait)
admin.site.register(models.Profession)
admin.site.register(models.Defence)
admin.site.register(models.DefenceType)
