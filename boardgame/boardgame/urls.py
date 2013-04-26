from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^cards/', include('cards.urls', 'cards', 'cards')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'', include('game.urls', 'game', 'game')),
)
