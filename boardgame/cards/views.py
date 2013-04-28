from collections import OrderedDict

from django.db.models import Max
from django.db.models.loading import get_model
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
from django.views.generic import DetailView, ListView

from game.models import Attribute


class HeroComponentMixin(object):

    def get(self, request, *args, **kwargs):
        self.empty_attribute_dict = self.get_empty_attribute_dict()
        return super(HeroComponentMixin, self).get(request, *args, **kwargs)

    def get_empty_attribute_dict(self):
        attributes = Attribute.objects.all()
        return OrderedDict([(i.name, None) for i in attributes])

    def get_queryset(self):
        model = self.get_model()
        queryset = model._default_manager.prefetch_related(
            'modifiers',
            'modifiers__attribute'
        )
        self.max_magnitude = queryset.aggregate(
            Max('modifiers__magnitude')
        ).get('modifiers__magnitude__max')
        return queryset
            
    def get_model(self):
        if self.model:
            return self.model
        try:
            model_name = self.kwargs['hero_component']
        except KeyError:
            raise ImproperlyConfigured(
                "{} must be passed a 'hero_component' kwarg".format(self.__class__)
            )
        else:
            model = self.get_model_by_name(model_name)
            if model:
                return model
            else:
                raise Http404

    def get_model_by_name(self, model_name):
        return get_model('cards', model_name)

    def get_context_data(self, *args, **kwargs):
        context = super(HeroComponentMixin, self).get_context_data(*args, **kwargs)
        context.update({
            'attributes': self.empty_attribute_dict.keys(),
            'max_magnitude': self.max_magnitude
        })
        return context


class HeroComponentListView(HeroComponentMixin, ListView):
    template_name = 'cards/hero_component_list.html'

    def get_queryset(self):
        queryset = super(HeroComponentListView, self).get_queryset()
        for obj in queryset:
            attrs = self.empty_attribute_dict.copy()
            for mod in obj.modifiers.all():
                attrs[mod.attribute.name] = mod
            obj.attributes = attrs
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(HeroComponentListView, self).get_context_data(*args, **kwargs)
        context.update({'title': self.kwargs.get('hero_component')})
        return context


class HeroComponentDetailView(HeroComponentMixin, DetailView):
    template_name = 'cards/hero_component_detail.html'

    def get_object(self, queryset=None):
        obj = super(HeroComponentDetailView, self).get_object(queryset)
        attrs = self.empty_attribute_dict.copy()
        for mod in obj.modifiers.all():
            attrs[mod.attribute.name] = mod
        obj.attributes = attrs
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(HeroComponentDetailView, self).get_context_data(*args, **kwargs)
        context.update({'title': self.object.name })
        return context
