from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass




class Todo(models.Model):
    COLOUR_CHOICES = (
        ("transparent", "None"),

        ("red", "Red"),
        ("green", "Green"),
        ("blue", "Blue"),
        ("yellow", "Yellow"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    colour = models.CharField(max_length=100, choices=COLOUR_CHOICES, default=COLOUR_CHOICES[0])
    deadline = models.DateTimeField(null=True,blank=True, default=None)
    completed = models.BooleanField(default=False)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


# Create your models here.
