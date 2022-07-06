from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    udirector = models.ForeignKey(Director, on_delete=models.CASCADE,
                             related_name="Director", null=True)
    image = models.ImageField(verbose_name="Картинка")

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                             related_name="Movie", null=True)


