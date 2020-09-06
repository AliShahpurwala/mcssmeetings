from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager
	)

import django.utils.timezone
# Create your models here.

class UserManager(BaseUserManager):
	def create_user(self, username, password):
		
		username = self.normalize_username(username)
		user = self.model(username=username)
		user.set_password(password)
		user.save()

		return user

class User(AbstractBaseUser):
	username = models.CharField(max_length=255, primary_key=True)
	administratorStatus = models.BooleanField(default=False)
	timeCreated = models.DateTimeField(default=timezone.now)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

