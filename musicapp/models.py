from django.db import models

# Create your models here.

class Artiste(models.Model):
    """Information about an artiste."""
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    age = models.IntegerField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.first_name


class Song(models.Model):
    """Songs by each artiste."""
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length = 40)
    date_released = models.DateField()

    class Meta:
        verbose_name_plural = 'songs'

    def __str__(self):
         """Return a string representation of the model."""
         return self.title


class Lyric(models.Model):
    """Specific lyric about a song."""
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'lyrics'

    def __str__(self):
         """Return a string representation of the model."""
         return f"{self.content[:50]}..."