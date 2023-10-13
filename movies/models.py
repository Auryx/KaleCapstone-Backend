from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    leadActor = models.CharField(max_length=100)
    release = models.CharField(max_length=100)
    pgRating = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=100)