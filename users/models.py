#from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    career_goal = models.CharField(max_length=200, blank=True)
    experience_level = models.CharField(max_length=100, blank=True)