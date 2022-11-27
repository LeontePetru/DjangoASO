from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    roomName = models.CharField(max_length=256)

class Message(models.Model):
    text = models.CharField(max_length=9999)
    user = models.CharField(max_length=256)
    date = models.DateTimeField(default=datetime.now)
    room = models.CharField(max_length=256)