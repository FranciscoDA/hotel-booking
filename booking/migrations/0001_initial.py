# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Guest'
        db.create_table('booking_guest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dni', self.gf('django.db.models.fields.IntegerField')(unique=True, blank=True, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True, null=True)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
        ))
        db.send_create_signal('booking', ['Guest'])

        # Adding model 'Booking'
        db.create_table('booking_booking', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.Guest'])),
            ('booked', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('last_mod', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('checkin', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('checkout', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('pax', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('obs', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('car', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('booking', ['Booking'])

        # Adding model 'Night'
        db.create_table('booking_night', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('booking', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.Booking'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.Room'])),
        ))
        db.send_create_signal('booking', ['Night'])

        # Adding unique constraint on 'Night', fields ['date', 'room']
        db.create_unique('booking_night', ['date', 'room_id'])

        # Adding model 'Room'
        db.create_table('booking_room', (
            ('number', self.gf('django.db.models.fields.PositiveSmallIntegerField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50, default='Matrimonial')),
            ('obs', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('booking', ['Room'])


    def backwards(self, orm):
        # Removing unique constraint on 'Night', fields ['date', 'room']
        db.delete_unique('booking_night', ['date', 'room_id'])

        # Deleting model 'Guest'
        db.delete_table('booking_guest')

        # Deleting model 'Booking'
        db.delete_table('booking_booking')

        # Deleting model 'Night'
        db.delete_table('booking_night')

        # Deleting model 'Room'
        db.delete_table('booking_room')


    models = {
        'booking.booking': {
            'Meta': {'object_name': 'Booking'},
            'booked': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'car': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'checkin': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'checkout': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'guest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['booking.Guest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obs': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'pax': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'booking.guest': {
            'Meta': {'object_name': 'Guest'},
            'dni': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'booking.night': {
            'Meta': {'object_name': 'Night', 'unique_together': "(('date', 'room'),)"},
            'booking': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['booking.Booking']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['booking.Room']"})
        },
        'booking.room': {
            'Meta': {'object_name': 'Room'},
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'primary_key': 'True'}),
            'obs': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'Matrimonial'"})
        }
    }

    complete_apps = ['booking']