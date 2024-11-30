from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.name
    

class Messages(models.Model):
    name = models.CharField(max_length=255)
    messages = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
