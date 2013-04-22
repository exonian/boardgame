# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Trait.modifiers'
        db.delete_column(u'cards_trait', 'modifiers_id')

        # Deleting field 'Profession.modifiers'
        db.delete_column(u'cards_profession', 'modifiers_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Trait.modifiers'
        raise RuntimeError("Cannot reverse this migration. 'Trait.modifiers' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Profession.modifiers'
        raise RuntimeError("Cannot reverse this migration. 'Profession.modifiers' and its values cannot be restored.")

    models = {
        u'cards.modifier': {
            'Meta': {'object_name': 'Modifier'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'modifiers'", 'to': u"orm['game.Attribute']"}),
            'component_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'component_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'magnitude': ('django.db.models.fields.FloatField', [], {}),
            'operator': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'cards.profession': {
            'Meta': {'object_name': 'Profession'},
            'flavour_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'special_rules': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'cards.trait': {
            'Meta': {'object_name': 'Trait'},
            'flavour_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'special_rules': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'game.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cards']