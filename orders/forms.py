from django import forms
from .models import Order
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['nome', 'sobrenome', 'email', 'endereco','codigo_postal', 'cidade']
