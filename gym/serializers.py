from rest_framework import serializers
from .models import (
    Member,
    Trainer,
    Exercise,
    WorkoutPlan,
    Session,
)


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class WorkoutPlanSerializer(serializers.ModelSerializer):

    exercises = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Exercise.objects.all()
    )

    class Meta:
        model = WorkoutPlan
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


