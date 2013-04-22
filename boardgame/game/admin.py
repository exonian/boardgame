from django.contrib import admin

from . import models

class GameAdmin(admin.ModelAdmin):
    filter_horizontal = ('attributes',)

admin.site.register(models.Game, GameAdmin)
admin.site.register(models.Attribute)
