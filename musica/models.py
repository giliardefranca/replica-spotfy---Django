from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

CATEGORIA = (
    ("BRAZIL", 'Brazil'),
    ("INTERNACIONAL", 'Internacional'),
    ("ROMANCE", 'Romance'),
    ("SERTANEJO", "Sertanejo"),
    ("POP", 'Pop'),
    ("FORRO", 'Forro'),
    ("FUNK", 'Funk')

)

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=CATEGORIA)
    thumb = models.ImageField(upload_to="upload_musica")

    def __str__(self):
        return self.titulo

class Musica(models.Model):
    album = models.ForeignKey("Album", related_name="musicas", on_delete=models.CASCADE)
    artista = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    musica = models.FileField()
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.album.titulo + "-" + self.titulo




class Usuario(AbstractUser):
    play_list = models.ManyToManyField('Album')
