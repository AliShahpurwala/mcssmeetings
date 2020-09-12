from django.db import models
from login.models import User
# Create your models here.
class meeting(models.Model):
	meetingHeader = models.CharField(max_length=255, default="")
	startTime = models.DateTimeField(blank=False)
	endTime = models.DateTimeField(blank=False)
	createdOn = models.DateTimeField(auto_now_add=True)
	attendedBy = models.ManyToManyField(User)

class agendaItem(models.Model):
	underMeeting = models.ForeignKey(meeting, on_delete=models.CASCADE, default=None)
	agendaHeader = models.CharField(max_length=255)
	agendaMainText = models.CharField(max_length=255)

	def compile_relevant_comments(self):
		compiled_comments = []
		for com in comment.objects.all():
			if com.underAgendaItem == self:
				compiled_comments.append(com)
		return compiled_comments

class comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	underAgendaItem = models.ForeignKey(agendaItem, on_delete=models.CASCADE)
	text = models.CharField(max_length=255)
