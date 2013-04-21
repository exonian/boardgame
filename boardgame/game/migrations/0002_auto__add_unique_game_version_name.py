# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Game', fields ['version', 'name']
        db.create_unique(u'game_game', ['version', 'name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Game', fields ['version', 'name']
        db.delete_unique(u'game_game', ['version', 'name'])


    models = {
        u'game.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'game.game': {
            'Meta': {'unique_together': "(('name', 'version'),)", 'object_name': 'Game'},
            'attributes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['game.Attribute']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['game']