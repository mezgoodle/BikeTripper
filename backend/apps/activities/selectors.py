from django.db.models import Sum, Avg, Count
from django.db.models.functions import Coalesce

from .models import Activity


def get_user_activity_stats(user):
    return Activity.objects.filter(user=user).aggregate(
        total_distance=Coalesce(Sum("distance_km"), 0.0),
        total_elevation=Coalesce(Sum("elevation_gain"), 0.0),
        total_time=Coalesce(Sum("duration_seconds"), 0),
        avg_speed=Coalesce(Avg("avg_speed"), 0.0),
        total_rides=Count("id"),
    )
