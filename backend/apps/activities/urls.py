from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ActivityViewSet, ActivityStatsView

router = DefaultRouter()
router.register("activities", ActivityViewSet, basename="activities")

urlpatterns = router.urls + [path("stats/", ActivityStatsView.as_view())]
