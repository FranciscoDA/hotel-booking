from django.contrib import admin
from booking.models import *


class NightInline(admin.StackedInline):
    model = Night


class BookingAdmin(admin.ModelAdmin):
    inlines = [NightInline]


admin.site.register(Room)
admin.site.register(Client)
admin.site.register(Booking, BookingAdmin)