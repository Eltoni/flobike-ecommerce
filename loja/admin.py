from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import*
# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome','slug']
    prepopulated_fields ={'slug':('nome',)}
admin.site.register(Categoria,CategoriaAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'preco', 'stock',
    'habilitado', 'criado', 'atualizado']
    list_filter = ['habilitado', 'criado', 'atualizado']
    list_editable = ['preco', 'stock','habilitado']
    prepopulated_fields = {'slug': ('nome',)}
admin.site.register(Produto, ProdutoAdmin)
