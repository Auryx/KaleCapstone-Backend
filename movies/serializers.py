from .models import Movie
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'lead_actor', 'release', 'pg_rating', 'synopsis']