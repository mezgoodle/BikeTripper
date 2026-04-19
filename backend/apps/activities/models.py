from django.conf import settings
from django.db import models

from apps.core.models import BaseModel


class Activity(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="activities"
    )
    title = models.CharField(max_length=255)
    distance_km = models.FloatField(null=True, blank=True)
    duration_seconds = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    avg_speed = models.FloatField(
        null=True,
        blank=True
    )
    elevation_gain = models.FloatField(
        null=True,
        blank=True
    )
    gpx_file = models.FileField(
        upload_to="gpx/",
        null=True,
        blank=True
    )
    polyline = models.TextField(
        blank=True
    )
    started_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user} - {self.title}"
