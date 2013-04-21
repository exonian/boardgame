from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255)
    version = models.CharField(max_length=15)
    attributes = models.ManyToManyField('Attribute',
                                        blank=True,
                                        null=True)


class Attribute(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=8)
