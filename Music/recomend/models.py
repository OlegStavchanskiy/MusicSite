from django.db import models


class Music(models.Model):
    path_to_song = models.CharField(max_length=128)
    path_to_img = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    artist = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)



