# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Trait'
        db.create_table(u'cards_trait', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('modifiers', self.gf('django.db.models.fields.related.ForeignKey')(related_name='related_traits', to=orm['cards.Modifier'])),
            ('special_rules', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('flavour_text', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'cards', ['Trait'])

        # Adding model 'Profession'
        db.create_table(u'cards_profession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('modifiers', self.gf('django.db.models.fields.related.ForeignKey')(related_name='related_professions', to=orm['cards.Modifier'])),
            ('special_rules', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('flavour_text', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'cards', ['Profession'])


    def backwards(self, orm):
        # Deleting model 'Trait'
        db.delete_table(u'cards_trait')

        # Deleting model 'Profession'
        db.delete_table(u'cards_profession')


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
            'modifiers': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_professions'", 'to': u"orm['cards.Modifier']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'special_rules': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'cards.trait': {
            'Meta': {'object_name': 'Trait'},
            'flavour_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifiers': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_traits'", 'to': u"orm['cards.Modifier']"}),
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