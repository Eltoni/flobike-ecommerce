from django.db import models

class Inscrever(models.Model):
    nome = models.CharField(verbose_name='Seu Nome',max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='E-mail')
    endereco = models.CharField(max_length=250,verbose_name='Endereço')
    #numero = models.CharField(max_length=20,verbose_name='Núremo da Casa')
    cidade = models.CharField(max_length=100)
    criado = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2,default=50.00)
    #updated = models.DateTimeField(auto_now=True)
    pago = models.BooleanField(default=False)
    class Meta:
        ordering = ('-criado',)


#inlines = [OrderItemInline]
#admin.site.register(Order, OrderAdmin)
