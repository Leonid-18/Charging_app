import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .constants import BILLING_ITEM_TYPES


class BillingItem(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)
    type = models.PositiveSmallIntegerField(null=True, blank=True, choices=BILLING_ITEM_TYPES)
    rate = models.PositiveSmallIntegerField(blank=False, null=True)
    amount = models.FloatField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    identifier = models.UUIDField(default=uuid.uuid4)
    transaction_id = models.CharField(max_length=250, null=True, blank=True)
    currency = models.CharField(max_length=10, null=False, blank=True)
    details = models.JSONField(default=dict, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        finished = " [FINISHED]" if self.cancelled_at else ""
        return f"{self.user}: {self.currency} created at {self.created_at} {finished}"
