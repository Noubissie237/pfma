from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.genre

    class Meta:
        db_table = 'Genres'
        verbose_name = "Genre"
        verbose_name_plural = ("Genres")

class Users(models.Model):
    nom = models.CharField(max_length=70)
    email = models.EmailField(max_length=254, unique=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    pwd = models.CharField(max_length=70)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "User"
        verbose_name_plural = ("Users")
        db_table = 'Users'

