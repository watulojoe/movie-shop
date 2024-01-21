from django.db import models


# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    img = models.URLField(blank=True, null=True)
    about = models.CharField(max_length=230, blank=True, null=True)
    runtime = models.CharField(max_length=20, blank=True, null=True)
    seasons = models.CharField(max_length=10, blank=True, null=True)
    genre = models.ManyToManyField(Genre, blank=True, null=True)
    movie_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


class Season(models.Model):
    title = models.CharField(max_length=20)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Episode(models.Model):
    title = models.CharField(max_length=20)
    movie_url = models.URLField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    # todo: add date updated

    def __str__(self):
        return f"{self.title}"

