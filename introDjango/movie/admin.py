from django.contrib import admin

# Register your models here.

from .models import Director, Genre, Pelicula

admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Pelicula)