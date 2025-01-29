from celery import shared_task

from analyzer import services


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 3, "countdown": 10},
)
def process_workout(self, workout_id):
    """Task for recalculation of rates"""
    try:
        services.recalculate_rates(workout_id)
        return f"Processed workout {workout_id}"
    except Exception as e:
        self.retry(exc=e)
        return f"Exception {e} raised while processing workout {workout_id}"
