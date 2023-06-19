from django.db import models

# Create your models here.

class Message(models.Model):
    username = models.CharField(default='',blank=False,max_length=200)
    room_name = models.CharField(default='',blank=False,max_length=200)
    message = models.CharField(default='',blank=False,max_length=200)

    # def __init__(self):
    #     return f'{self.username},{self.room_name}'
