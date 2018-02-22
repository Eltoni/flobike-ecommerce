from django.contrib import admin

from app.models import*
# Register your models here.

class TopicoAdmin( admin.ModelAdmin ):
	list_display = ('texto','data_add')
	prepopulated_fields = {'slug': ("texto",)} # preencher automáticamente slug baseado no título

admin.site.register(Topico, TopicoAdmin )

admin.site.register(Carousel)
