from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from .views import dashboard_stats

from .views import (
    MemberViewSet,
    TrainerViewSet,
    ExerciseViewSet,
    WorkoutPlanViewSet,
    SessionViewSet,
)


router = DefaultRouter()

router.register("members", MemberViewSet)
router.register("trainers", TrainerViewSet)
router.register("exercises", ExerciseViewSet)
router.register("workout-plans", WorkoutPlanViewSet)
router.register("sessions", SessionViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("dashboard/", dashboard_stats),
]