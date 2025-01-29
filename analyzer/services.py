from django.db.models import Avg, Max

from analyzer.models import Workout, Sample


def recalculate_rates(workout_id: int):
    """Recalculate rates for a workout given by workout_id."""

    workout = Workout.objects.get(id=workout_id)
    samples = Sample.objects.filter(workout=workout).aggregate(
        avg_heart_rate=Avg("heart_rate"), max_heart_rate=Max("heart_rate")
    )

    workout.avg_heart_rate = samples["avg_heart_rate"]
    workout.max_heart_rate = samples["max_heart_rate"]
    workout.save()
