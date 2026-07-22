from django.shortcuts import render

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


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


