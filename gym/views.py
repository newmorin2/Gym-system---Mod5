from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework import viewsets

from .models import (
    Member,
    Trainer,
    Exercise,
    WorkoutPlan,
    Session,
)

from .serializers import (
    MemberSerializer,
    TrainerSerializer,
    ExerciseSerializer,
    WorkoutPlanSerializer,
    SessionSerializer,
)

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [IsAuthenticated]

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAuthenticated]

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    data = {
        "members": Member.objects.count(),
        "trainers": Trainer.objects.count(),
        "exercises": Exercise.objects.count(),
        "workout_plans": WorkoutPlan.objects.count(),
        "sessions": Session.objects.count(),
    }
    return Response(data)