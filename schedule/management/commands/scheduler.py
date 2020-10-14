import logging

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore #, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
import sys
from django.core.management.base import BaseCommand, CommandError

# This is the function you want to schedule - add as many as you want and then register them in the start() function below
def check_appointment():
    #today = timezone.now()
    #appointment_time_start = timezone.now()
    #if appointment_time_start == today:
    #time.sleep(4)
    print('It is Time!')
    file=open(r'C:\\Users\Claude\Desktop\UoN\UeCv2\myfile.txt','w')
    file.write('this is the job')
    file.close()


class Command(BaseCommand):

    def handle(self, *args, **options):

        scheduler = BackgroundScheduler()
        scheduler.add_jobstore(DjangoJobStore(), "default")
        # run this job every 24 hours
        scheduler.add_job(check_appointment, 'interval', minutes=1, name='check_appointment', jobstore='default')
        #register_events(scheduler)
        #scheduler.start()
        #self.stdout.write('scheduler started!')

        try:
            self.stdout.write('scheduler started!')
            scheduler.start()
        except KeyboardInterrupt:
            #logger.info("Stopping scheduler...")
            scheduler.shutdown()
            self.stdout.write('scheduler stopped!')
