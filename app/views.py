from django.shortcuts import render
from .models import*
from .forms import*
# Create your views here.
def index(request):
    carousel = Carousel.objects.all()
    context = {'carousel':carousel
    }
    return render(request,"app/index.html",context)
def contato(request):
    return render(request,"app/contato.html")


def modalidade(request):
    return render(request,"app/modalidades.html")

def patrocinadores(request):
    return render(request,"app/patrocinadores.html")


def empresa(request):
    return render(request,"app/empresa.html")

#def produtos(request):
#    return render(request,"app/produtos.html")

def contato(request):
    context= {}
    if request.method =='POST':
        form = Contato(request.POST)
        if form.is_valid():
            context['is_valid']= True
            form.send_mail()
            form = Contato()
    else:
        form = Contato()
    context['form']= form
    return render(request,'app/contato.html',context)
