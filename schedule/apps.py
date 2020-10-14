from django.apps import AppConfig
from django.conf import settings

class ScheduleConfig(AppConfig):
    name = "schedule"

    def ready(self):
        from schedule import scheduler
        #scheduler = BackgroundScheduler()
        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()