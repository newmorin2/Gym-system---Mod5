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

class ExerciseNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ["id", "name"]

class WorkoutPlanSerializer(serializers.ModelSerializer):

    exercises = ExerciseNameSerializer(many=True, read_only=True)

    exercise_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Exercise.objects.all(),
        source="exercises",
        write_only=True
    )

    class Meta:
        model = WorkoutPlan
        fields = [
            "id",
            "title",
            "description",
            "difficulty",
            "exercises",
            "exercise_ids",
        ]


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


