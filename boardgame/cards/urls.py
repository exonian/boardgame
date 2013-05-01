from django.conf.urls import patterns, include, url
from django.views.generic import ListView, TemplateView

import views

urlpatterns = patterns('',
    url(r'^$', 
        TemplateView.as_view(template_name='cards/index.html'),
        name='index',
    ),
    url(r'^(?P<hero_component>trait|profession)/', include(patterns('',
        url(r'^$',
            views.HeroComponentListView.as_view(),
            name='hero-component-list',
        ),
        url(r'^(?P<pk>\d+)/$',
            views.HeroComponentDetailView.as_view(),
            name='hero-component-detail',
        ),
    ))),
    url(r'^defence/', include(patterns('',
        url(r'^$',
            views.DefenceListView.as_view(),
            name='defence-list',
        ),
        url(r'^(?P<pk>\d+)/$',
            views.DefenceDetailView.as_view(),
            name='defence-detail',
        ),
    ))),
)
