from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255)
    version = models.CharField(max_length=15)
    attributes = models.ManyToManyField('Attribute',
                                        blank=True,
                                        null=True)

    def __unicode__(self):
        return u'{} {}'.format(self.title, self.version)


class Attribute(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=8)

    def __unicode__(self):
        return self.name
