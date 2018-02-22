from django.contrib import admin
from .models import*
# Register your models here.
class InscreverAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'sobrenome', 'email',
    'endereco', 'cidade', 'pago',
    'criado','valor']
    list_filter = ['pago', 'criado',]

admin.site.register(Inscrever, InscreverAdmin)
