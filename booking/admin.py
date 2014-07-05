from django.contrib import admin
from booking.models import *


class NightInline(admin.TabularInline):
    model = Night
    extra = 1


class BookingAdmin(admin.ModelAdmin):
    list_display = ('guest', 'checkin', 'checkout', 'pax', 'booked', 'last_mod')
    search_fields = ['guest__name', 'checkin'] # Guest dni might also be a good idea
    raw_id_fields = ('guest',)
    inlines = [NightInline]


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'dni', 'email', 'phone', 'book', 'booking_history')
    search_fields = ['name', 'dni']

admin.site.register(Room)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Booking, BookingAdmin)
