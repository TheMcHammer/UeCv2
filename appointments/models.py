from django.conf import settings
from django.db import models


class AppointRequest(models.Model):
	to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
	from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user',on_delete=models.CASCADE)
	timestamp = models.DateTimeField() # set when appointment made

	def __str__(self):
		return "From {}, to {}".format(self.from_user.username, self.to_user.username)