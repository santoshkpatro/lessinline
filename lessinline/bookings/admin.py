from django.contrib import admin
from .models import BookingRequest, Booking


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ['service', 'user', 'slot', 'status', 'created_at']


@admin.register(Booking)
class Booking(admin.ModelAdmin):
    list_display = ['service', 'user', 'slot', 'status', 'created_at']
