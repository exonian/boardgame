from django.conf.urls import patterns, include, url
from django.views.generic import ListView, TemplateView

import views

urlpatterns = patterns('',
    url(r'^$', 
        TemplateView.as_view(template_name='cards/index.html'),
        name='index',
    ),
    url(r'^(?P<hero_component>[a-zA-Z]+)/$', 
        views.HeroComponentListView.as_view(),
        name='hero-component-list',
    ),
    url(r'^(?P<hero_component>[a-zA-Z]+)/(?P<pk>\d+)/$', 
        views.HeroComponentDetailView.as_view(),
        name='hero-component-detail',
    ),
)
