from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    lead_actor = models.CharField(max_length=100)
    release = models.CharField(max_length=100)
    pg_rating = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=100)