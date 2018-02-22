from django import forms
from django.core.mail import send_mail
from django.conf import settings
class Contato(forms.Form):
    nome= forms.CharField(label='Nome', max_length=200)
    email = forms.EmailField(label='E-mail')
    telefone = forms.CharField(label='Telefone')
    mensagem = forms.CharField(
        label='Mensagem',
        widget = forms.Textarea
    )
    def send_mail(self):
        subject = 'Contato flobike'
        mensagem = 'Nome: %(nome)s; E-mail: %(email)s;%(mensagem)s Telefone: %(telefone)s'
        context ={
            'nome':self.cleaned_data['nome'],
            'email':self.cleaned_data['email'],
            'mensagem':self.cleaned_data['mensagem'],
            'telefone':self.cleaned_data['telefone'],
        }
        mensagem = mensagem % context
        send_mail(subject,mensagem,settings.DEFAUL_FROM_EMAIL,[settings.CONTACT_EMAIL])
