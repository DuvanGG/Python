from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=64, help_text="Nombre del director")

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Nombre del genero de la pelicula")

    def __str__(self):
        return self.name

class Pelicula(models.Model):
    name = models.CharField(max_length=32, help_text="Nombre de la pelicula")
    description = models.TextField(max_length=100, help_text="Nombre de la pelicula")
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name