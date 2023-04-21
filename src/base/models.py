from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank = True, null=True)
    updated = models.DateTimeField(auto_now=True)      #Save the time when the object is updated
    cerated = models.DateTimeField(auto_now_add=True)  #Save the time when the object is created

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-updated', '-cerated']

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #related_name is used to access the messages from the room
    updated = models.DateTimeField(auto_now=True)      #Save the time when the object is updated
    cerated = models.DateTimeField(auto_now_add=True)  #Save the time when the object is created

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering = ['-updated', '-cerated']

class UserLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return self.user

class SignUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return self.user



class Test(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.username
