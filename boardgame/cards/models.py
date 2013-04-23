from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models

from game.models import Attribute, Game


class Modifier(models.Model):

    PLUS = '+'
    MINUS = '-'
    TIMES = '*'
    DIVIDE = '/'
    EQUALS = '='

    OPERATOR_CHOICES = (
        (PLUS, PLUS),
        (MINUS, MINUS),
        (TIMES, TIMES),
        (DIVIDE, DIVIDE),
        (EQUALS, EQUALS),
    )

    COMPONENT_TYPE_CHOICES = {"model__in": [
        'trait',
        'profession',
    ]}

    attribute = models.ForeignKey(Attribute, related_name='modifiers')
    operator = models.CharField(max_length=1, choices=OPERATOR_CHOICES)
    magnitude = models.FloatField()
    component_type = models.ForeignKey(
        ContentType,
        limit_choices_to=COMPONENT_TYPE_CHOICES,
        blank=True,
        null=True,
    )
    component_id = models.PositiveIntegerField(blank=True, null=True)
    component = generic.GenericForeignKey('component_type',
                                          'component_id')

    def __unicode__(self):
        return u'{} {} {}'.format(self.attribute, self.operator, self.magnitude)


class HeroComponent(models.Model):

    name = models.CharField(max_length=50)
    modifiers = generic.GenericRelation(Modifier,
                                        content_type_field="component_type",
                                        object_id_field="component_id")
    special_rules = models.TextField(blank=True)
    flavour_text = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'{}'.format(self.name)


class Trait(HeroComponent):
    pass


class Profession(HeroComponent):
    pass


class DefenceType(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'{}'.format(self.name)
