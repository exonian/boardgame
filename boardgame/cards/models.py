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

    attribute = models.ForeignKey(Attribute, related_name='modifiers')
    operator = models.CharField(max_length=1, choices=OPERATOR_CHOICES)
    magnitude = models.FloatField()

    def __unicode__(self):
        return u'{} {} {}'.format(self.attribute, self.operator, self.magnitude)
