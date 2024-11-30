from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import datetime
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=264, unique=True)
    

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User , on_delete=models.SET_NULL,null = True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic , on_delete=models.SET_NULL , null = True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # created_date = models.DateTimeField(default=datetime.now)  # Use default=datetime.now for flexibility
    # updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]

