from django.db import models
from django.conf import settings
# Create your models here.

class Todo(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	content = models.CharField(max_length=500) # write the schedule of the day
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.content)

