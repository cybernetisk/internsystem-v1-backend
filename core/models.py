from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Semester(models.Model):
    date_start = models.DateTimeField(blank=True)
    date_end = models.DateTimeField(blank=True)

class CybUser(models.Model):
    user = models.OneToOneField(User)
