from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Activity
from .serializers import ActivitySerializer
from .services import parse_gpx


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@action(detail=True, methods=["post"])
def upload_gpx(self, request, pk=None):
    activity = self.get_object()

    gpx_file = request.FILES.get("file")

    if not gpx_file:
        return Response(
            {"error": "No file provided"},
            status=status.HTTP_400_BAD_REQUEST
        )

    stats = parse_gpx(gpx_file)

    activity.gpx_file = gpx_file
    activity.distance_km = stats["distance_km"]
    activity.duration_seconds = stats["duration_seconds"]
    activity.avg_speed = stats["avg_speed"]
    activity.elevation_gain = stats["elevation_gain"]
    activity.polyline = stats["polyline"]

    activity.save()

    return Response(stats)
