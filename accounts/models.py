from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True, unique=True)
    profile_pic = models.ImageField(default="img-xiii.jpg", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Setting(models.Model):
    STATUS = (
        ('darkmode', 'darkmode'), 
        ('lightmode', 'lightmode'),
    )
    darkmode = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.darkmode

class AnimeInfo(models.Model):
    STATUS_GENRE = (
        ('0', 'Horror'), 
        ('1', 'Drama'), 
        ('2', 'Fantasy'), 
        ('3', 'Supernatural'), 
        ('4', 'Tragedy'),
    )
    STATUS_STATUS = (
        ('0', 'Still Airing'), 
        ('1', 'Completed'),
    )
    STATUS_RATING = (
        ('1', '1'), 
        ('2', '2'), 
        ('3', '3'), 
        ('4', '4'), 
        ('5', '5'),
    )

    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=300, null=True)
    genre = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=20, choices=STATUS_STATUS, default=None, blank=False, null=True)
    rating = models.CharField(max_length=1, choices=STATUS_RATING, default=None, blank=False, null=True)
    reviews = models.CharField(max_length=200, null=True)
    date_aired = models.DateField(max_length=200, null=True)
    season = models.CharField(max_length=200, null=True)

    # number = models.AutoField( null=True)
    
    def __str__(self): 
        return self.name