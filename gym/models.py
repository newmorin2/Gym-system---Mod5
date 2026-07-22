from django.db import models

# Create your models here.
from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    membership_type = models.CharField(max_length=50)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    equipment_needed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)

    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.title


class Session(models.Model):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE
    )

    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE
    )

    date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.member} - {self.date}"


