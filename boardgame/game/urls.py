from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from .models import Game

urlpatterns = patterns('',
    url(r'^$', 
        ListView.as_view(model=Game),
        name='game-list',
    ),
)
