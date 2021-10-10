from django.contrib import admin
from lessinline.services.models import Service, Slot


class SlotAdmin(admin.TabularInline):
    model = Slot
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'business', 'price', 'is_open']
    inlines = [SlotAdmin]
