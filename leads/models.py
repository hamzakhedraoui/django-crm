from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass


class Lead(models.Model):
    """
    SOURCES = (
        ('youtube', 'youtube'),
        ('facebook', 'facebook'),
        ('google', 'google')
    )
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    """    
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCES, max_length=100)
    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)
    """


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
