from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Member,
    Trainer,
    Exercise,
    WorkoutPlan,
    Session,
)


admin.site.register(Member)
admin.site.register(Trainer)
admin.site.register(Exercise)
admin.site.register(WorkoutPlan)
admin.site.register(Session)