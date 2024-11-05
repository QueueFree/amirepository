from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    objects = models.Manager()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    objects = models.Manager()


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    objects = models.Manager()

