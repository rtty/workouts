from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Workout, Sample
from .tasks import process_workout


@receiver(post_save, sender=Sample)
def schedule_workout_processing(sender, instance, created, **kwargs):
    if created:
        process_workout.delay(instance.workout_id)
