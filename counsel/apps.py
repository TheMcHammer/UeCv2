from django.apps import AppConfig
from django.conf import settings

class CounselConfig(AppConfig):
    name = "counsel"

    def ready(self):
        from schedule import scheduler
        #scheduler = BackgroundScheduler()
        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()