from django.db import models

# Create your models here.
from django.db import models
from django.http import HttpResponseRedirect,Http404
from django.shortcuts import render,reverse

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)
    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    def __str__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('loja:lista_produto_categoria', args =[self.slug])

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria,related_name='produtos',on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    #imagem = models.ImageField(upload_to='produtos/%Y/%m/%d',blank=True)
    imagem = models.ImageField()
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    habilitado = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('nome',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.nome

    def get_absolute_url(self):
       return reverse('loja:detalhes_produto', args =[self.id,self.slug])
