import uuid
from django.db import models
from django.conf import settings
from lessinline.services.models import Service, Slot


class BookingRequest(models.Model):
    STATUS_CHOICES = (
        ('REQUESTED', 'REQUESTED'),
        ('APPROVED', 'APPROVED'),
        ('DECLINED', 'DECLINED'),
        ('REPORT', 'REPORT'),
        ('CONFLICT', 'CONFLICT'),
        ('OTHER', 'OTHER')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    slot = models.ForeignKey(Slot, on_delete=models.SET_NULL, null=True)
    user_note = models.TextField(blank=True, null=True)
    business_note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, default='REQUESTED', choices=STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'booking_requests'

    def __str__(self) -> str:
        return 'Booking request for ' + self.service.name


class Booking(models.Model):
    STATUS_CHOICES = (
        ('CONFIRMED', 'CONFIRMED'),
        ('PENDING', 'PENDING'),
        ('CANCELLED', 'CANCELLED'),
        ('REPORT', 'REPORT'),
        ('CONFLICT', 'CONFLICT'),
        ('OTHER', 'OTHER')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    slot = models.ForeignKey(Slot, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, default='CONFIRMED', choices=STATUS_CHOICES)
    note = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bookings'

    def __str__(self) -> str:
        return str(self.id)
