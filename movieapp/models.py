from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=39)

    def __str__(self):
        return self.name

    objects = models.Manager()


class Movie(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    duration = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

    objects = models.Manager()


STARS = ((i, '* ' * i) for i in range(1, 6))


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=0, max_length=5)

    def __str__(self):
        return self.text

    objects = models.Manager()


