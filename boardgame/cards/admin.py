from django.contrib import admin

from . import models

admin.site.register(models.Modifier)
admin.site.register(models.Trait)
admin.site.register(models.Profession)
