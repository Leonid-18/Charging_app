from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group


class Rate(models.Model):
    group = models.ForeignKey(Group, null=False, blank=False, on_delete=models.PROTECT)
    rate = models.PositiveSmallIntegerField(null=False, blank=False)
    currency = models.CharField(max_length=10, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.group}: rate -> {self.rate} {self.currency} created at {self.created_at}"
