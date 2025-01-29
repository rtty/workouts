from django.core.management.base import BaseCommand
from analyzer.models import Workout, Sample
from django.contrib.auth.models import User
import random
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = "Generates samples"

    def handle(self, *args, **kwargs):
        user = User.objects.first() or User.objects.create(username="testuser")

        workouts = []
        for _ in range(100):
            workouts.append(
                Workout.objects.create(
                    user=user,
                    date=datetime.now() - timedelta(days=random.randint(1, 30)),
                )
            )

        for i in range(100):
            for workout in workouts:
                Sample(
                    workout=workout,
                    timestamp=workout.date + timedelta(seconds=i * 10),
                    heart_rate=random.randint(60, 180),
                ).save()

        self.stdout.write("10,000 samples generated")
