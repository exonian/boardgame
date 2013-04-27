from django import template
from django.template.loader import get_template

register = template.Library()


@register.inclusion_tag('cards/_modifier_td.html')
def modifier_td(modifier):
    return {'modifier': modifier}
