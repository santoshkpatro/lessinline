import uuid
from django.db import models
from lessinline.business.models import Business


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    advance_booking_days = models.PositiveSmallIntegerField(default=0)
    is_open = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'services'

    def __str__(self) -> str:
        return self.name


class Slot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    is_open = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'slots'

    def __str__(self) -> str:
        return 'slot of ' + self.service.name
