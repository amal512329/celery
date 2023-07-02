from celery import shared_task
from time import sleep
@shared_task
def go_to_sleep(duration):
    sleep(duration)
    return 'Done'