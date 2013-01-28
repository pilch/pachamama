# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'reviews_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'reviews', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'reviews_person')


    models = {
        u'reviews.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['reviews']