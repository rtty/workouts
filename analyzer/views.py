from rest_framework import viewsets

from analyzer.models import Workout, Sample
from analyzer.serializers import WorkoutSerializer, SampleSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all().order_by("-date")
    serializer_class = WorkoutSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
