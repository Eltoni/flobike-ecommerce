from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_POST
from inscrever.models import Inscrever
from .carrega import Carrega
#from .forms import CarregaAddInscreverForm


#@require_POST
def carrega_add(request,inscrever_id=1):
    carrega = Carrega(request)
    inscrever = get_object_or_404(Inscrever, id=inscrever_id)
    #form = CarregaAddInscreverForm(request.POST)
    #cd = form.cleaned_data
    carrega.add(inscrever=inscrever,valor=50)
    return redirect('carrega:carrega_detalhes')

def carrega_detalhes(request):
    carrega = Carrega(request)
    return render(request, 'carrega/detalhes.html', {'carrega': carrega})
