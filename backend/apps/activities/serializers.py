from rest_framework import serializers

from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"
        read_only_fields = ["user"]


class ActivityStatsSerializer(serializers.Serializer):
    total_distance = serializers.FloatField()
    total_elevation = serializers.FloatField()
    total_time = serializers.IntegerField()
    avg_speed = serializers.FloatField()
    total_rides = serializers.IntegerField()
