from django.contrib import admin
from booking.models import *


class OccupancyAdmin(admin.ModelAdmin):
    list_display = ('date', 'room', 'guest', 'obs')
    search_fields = ['date']
    def guest(self, obj):
        return obj.booking.guest
    guest.admin_order_field = 'booking__guest'


class OccupancyInline(admin.TabularInline):
    model = Occupancy
    extra = 1


class BookingAdmin(admin.ModelAdmin):
    list_display = ('guest', 'checkin', 'checkout', 'pax', 'booked', 'last_mod')
    search_fields = ['guest__first_name', 'guest__last_name', 'checkin'] # Guest dni might also be a good idea
    raw_id_fields = ('guest',)
    inlines = [OccupancyInline]


class GuestAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'nid', 'email', 'tel', 'book', 'booking_history')
    search_fields = ['first_name', 'last_name', 'nid']


admin.site.register(Room)
admin.site.register(Occupancy, OccupancyAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Booking, BookingAdmin)
