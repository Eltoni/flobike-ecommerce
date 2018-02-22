from django import forms
from .models import Inscrever
class InscreverCreateForm(forms.ModelForm):
    class Meta:
        model = Inscrever
        fields = ['nome', 'sobrenome', 'email', 'endereco',
         'cidade']
