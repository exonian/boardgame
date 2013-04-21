from django.db import models


class GameManager(models.Manager):
    def get_by_natural_key(self, name, version):
        return self.get(name=name, version=version)


class Game(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=15)
    attributes = models.ManyToManyField('Attribute',
                                        blank=True,
                                        null=True)

    objects = GameManager()

    class Meta:
        unique_together = ('name', 'version')

    def __unicode__(self):
        return u'{} {}'.format(self.name, self.version)

    def natural_key(self):
        return (self.name, self.version)


class AttributeManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name,)


class Attribute(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=8)

    objects = AttributeManager()

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return (self.name,)
