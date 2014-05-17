from django.contrib import admin
from booking.models import *


class NightInline(admin.StackedInline):
    model = Night


class BookingAdmin(admin.ModelAdmin):
    list_display = ('client', 'booked')
    inlines = [NightInline]


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'dni', 'email', 'phone')
    search_fields = ['name', 'dni']

admin.site.register(Room)
admin.site.register(Client, ClientAdmin)
admin.site.register(Booking, BookingAdmin)