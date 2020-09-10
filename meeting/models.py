from django.db import models
from login.models import User
# Create your models here.
class meeting(models.Model):
	startTime = models.DateTimeField(blank=False)
	endTime = models.DateTimeField(blank=False)
	createdOn = models.DateTimeField(auto_now_add=True)
	attendedBy = models.ManyToManyField(User)