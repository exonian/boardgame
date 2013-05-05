from math import ceil

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


@register.inclusion_tag('cards/_hero_component_probabilities_table.html', takes_context=True)
def hero_component_probabilities_table(context):
    return {
        'attribute_probabilities': context['attribute_probabilities'],
        'targets': context['targets'],
        'max_magnitude': context['max_magnitude'],
    }


@register.simple_tag(takes_context=True)
def modifier_css_class(context, modifier):
    if not modifier:
        return ''
    magnitude = modifier.magnitude
    max_magnitude = context['max_magnitude']
    percentage = 100 * float(magnitude)/max_magnitude
    step_size = 10
    rounded_percentage = int(step_size * ceil(percentage / step_size))
    return '{css_class} {css_class}-{percentage}'.format(**{
        'css_class': modifier.css_class,
        'percentage': rounded_percentage,
    })
