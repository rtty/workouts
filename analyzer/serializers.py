from rest_framework import serializers
from analyzer.models import Workout, Sample


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ["timestamp", "heart_rate"]


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ["id", "user", "avg_heart_rate", "max_heart_rate", "date"]
