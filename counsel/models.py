from django.db import models
from django.conf import settings
import datetime
from django_messages.models import Message
# Database creation for teacher appintment.
class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    time_start = models.CharField(max_length=50)
    time_end = models.CharField(max_length=50)
    room_number = models.CharField(max_length=50)
    appointment_with = models.CharField(max_length=50, blank=True)
    update_time = models.DateField(auto_now=True, auto_now_add=False)
    frist_time = models.DateField(auto_now=False, auto_now_add=True)
    message = models.ForeignKey(Message,  blank=True, null=True, on_delete = models.CASCADE)

    # show filed in admin panel
    def __str__(self):
        return self.date

    def __str__(self):
        return self.time_start

    def __str__(self):
        return self.time_end

    #def __str__(self):
    #    return self.room_number

    def __str__(self):
        return self.appointment_with

'''
class AppointmentToMessage(models.Model):
    appointment = models.ForeignKey(Appointment, related_name='applied_to')
    message = models.ForeignKey(Message, related_name='from_user')
    STATUS_CHOICES = (
       ('1', 'Booked'),
       ('2', 'Not Booked'),
       ('3', 'Ready')
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ("appointment", "message")
'''

class Questions(models.Model):
    PROBLEM_CHOICES = (
        ('lonely','lonely'),
        ('eating', 'eating'),
        ('worry','worry')
               )

    PARENT_CHOICES = (
        ('father','father'),
        ('mother','mother'),
        ('both','both'),
        ('none','none')
    )
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    problems = models.CharField(max_length=200, choices= PROBLEM_CHOICES, null=True, blank=True)
    parents = models.CharField(max_length=200, choices= PARENT_CHOICES, null=True, blank=True)
    siblings = models.IntegerField(default=0)
    relationship = models.BooleanField(default=False)