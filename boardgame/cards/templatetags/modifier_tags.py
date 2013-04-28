from django import template
from django.template.loader import get_template

register = template.Library()


@register.inclusion_tag('cards/_hero_component_table.html', takes_context=True)
def hero_component_table(context, components):
    try:
        is_iterable = iter(components)
    except TypeError:
        # if we were given a single instance of a component, we can just
        # put it in a single-item list and then not worry about it
        components = [components]
    return {
        'components': components,
        'attributes': context['attributes'],
        'max_magnitude': context['max_magnitude'],
    }
