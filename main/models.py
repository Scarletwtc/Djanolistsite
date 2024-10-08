from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length= 200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist', null=True)


    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE) #on delete delets iytems if the todolist is deleted
    text = models.CharField(max_length= 400)
    complete= models.BooleanField()

    def __str__(self):
        return self.text


