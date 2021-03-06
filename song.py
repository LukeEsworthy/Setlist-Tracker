from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=75)
    artist = models.CharField(max_length=75)
    song_length = models.IntegerField()

    def __str__(self):
        return f'{self.title} by {self.artist}'
