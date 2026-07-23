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

class MemberNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ["id", "name"]

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"

class TrainerNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = ["id", "name"]

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

    member = MemberNameSerializer(read_only=True)
    trainer = TrainerNameSerializer(read_only=True)

    member_id = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(),
        source="member",
        write_only=True
    )

    trainer_id = serializers.PrimaryKeyRelatedField(
        queryset=Trainer.objects.all(),
        source="trainer",
        write_only=True
    )

    class Meta:
        model = Session
        fields = [
            "id",
            "member",
            "trainer",
            "member_id",
            "trainer_id",
            "date",
            "status"
        ]


