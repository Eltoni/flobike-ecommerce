from django.db import models
from django.db.models import ImageField,SlugField
# Create your models here.

# Model do Carousel
class Carousel(models.Model):
    """ Serão Inseridos as imagens e os textos no carousel data que vai permanacer """
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    imagem = models.ImageField()
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_final = models.DateTimeField()
    def __str__(self):
        """ Devolve uma representação em String modelo"""
        return self.titulo
#imagem = models.ImageField(upload_to = "blog/uploads/postagem",blank=True)
class Topico(models.Model):
    texto = models.CharField(max_length=15)
    data_add = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug / URL", help_text="Preenchido automaticamente, não editar.",)
    def __str__(self):
        """ Devolve uma representação em String modelo"""
        return self.texto
