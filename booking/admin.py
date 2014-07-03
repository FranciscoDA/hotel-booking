from django.contrib import admin
from booking.models import *


class NightInline(admin.StackedInline):
    model = Night


class BookingAdmin(admin.ModelAdmin):
    list_display = ('guest', 'checkin', 'checkout', 'pax', 'booked', 'last_mod')
    search_fields = ('guest',)
    raw_id_fields = ('guest',)
    inlines = [NightInline]


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'dni', 'email', 'phone', 'book', 'details')
    search_fields = ['name', 'dni']

admin.site.register(Room)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Booking, BookingAdmin)