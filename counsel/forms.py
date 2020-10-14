from django import forms
from .models import Appointment, Questions

class AppointmentForm(forms.ModelForm):
	class Meta:
		model=Appointment
		fields=[
		    "date",
		    "time_start",
		    "time_end",
		    "room_number",
		    "appointment_with"
		]

class Pre_counsellingForm(forms.ModelForm):
	class Meta:
		model=Questions
		fields=[
			"problems",
			"parents",
			"siblings",
			"relationship"
		]