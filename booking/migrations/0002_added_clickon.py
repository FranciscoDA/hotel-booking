# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Booking.clickon'
        db.add_column('booking_booking', 'clickon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Booking.clickon'
        db.delete_column('booking_booking', 'clickon')


    models = {
        'booking.booking': {
            'Meta': {'object_name': 'Booking'},
            'booked': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'checkin': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'checkout': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'clickon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'guest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['booking.Guest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obs': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'pax': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'})
        },
        'booking.guest': {
            'Meta': {'object_name': 'Guest'},
            'dni': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'unique': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'booking.night': {
            'Meta': {'unique_together': "(('date', 'room'),)", 'object_name': 'Night'},
            'booking': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['booking.Booking']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['booking.Room']"})
        },
        'booking.room': {
            'Meta': {'object_name': 'Room'},
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'primary_key': 'True'}),
            'obs': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Matrimonial'", 'max_length': '50'})
        }
    }

    complete_apps = ['booking']