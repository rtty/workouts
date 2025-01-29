from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    """Workout model"""

    user: models.ForeignKey[User] = models.ForeignKey(User, on_delete=models.CASCADE)
    date: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    avg_heart_rate: models.FloatField = models.FloatField(null=True)
    max_heart_rate: models.FloatField = models.FloatField(null=True)

    class Meta:
        db_table = "workouts"


class Sample(models.Model):
    """Sample model"""

    workout: models.ForeignKey[Workout] = models.ForeignKey(
        Workout, on_delete=models.CASCADE
    )
    timestamp: models.DateTimeField = models.DateTimeField()
    heart_rate: models.IntegerField = models.IntegerField()

    class Meta:
        db_table = "samples"
