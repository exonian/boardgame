from django.db.models.loading import get_model
from django.http import Http404
from django.views.generic import DetailView, ListView


class HeroComponentMixin(object):

    def get_queryset(self):
        model = self.get_model()
        queryset = model._default_manager.all()
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


class HeroComponentListView(HeroComponentMixin, ListView):
    template_name = 'cards/hero_component_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HeroComponentListView, self).get_context_data(*args, **kwargs)
        context.update({'title': self.kwargs.get('hero_component')})
        return context


class HeroComponentDetailView(HeroComponentMixin, DetailView):
    template_name = 'cards/hero_component_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HeroComponentDetailView, self).get_context_data(*args, **kwargs)
        context.update({'title': self.object.name })
        return context
