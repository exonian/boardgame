# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'game_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'game', ['Game'])

        # Adding M2M table for field attributes on 'Game'
        db.create_table(u'game_game_attributes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm[u'game.game'], null=False)),
            ('attribute', models.ForeignKey(orm[u'game.attribute'], null=False))
        ))
        db.create_unique(u'game_game_attributes', ['game_id', 'attribute_id'])

        # Adding model 'Attribute'
        db.create_table(u'game_attribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal(u'game', ['Attribute'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'game_game')

        # Removing M2M table for field attributes on 'Game'
        db.delete_table('game_game_attributes')

        # Deleting model 'Attribute'
        db.delete_table(u'game_attribute')


    models = {
        u'game.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'game.game': {
            'Meta': {'object_name': 'Game'},
            'attributes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['game.Attribute']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['game']