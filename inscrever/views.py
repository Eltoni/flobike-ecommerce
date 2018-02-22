from django.shortcuts import render,redirect,reverse
#from django.core.urlresolvers import reverse
from .models import*
from .forms import*
#from cart.cart import Cart
#from .tasks import order_created
# Create your views here.

def inscrito(request):
    #cart = Cart(request)
    if request.method != 'POST':
        form = InscreverCreateForm()
    else:
        form = InscreverCreateForm(request.POST)
        if form.is_valid():
            #order = form.save()
            inscrever = form.save(commit=False)
            inscrever.save()
            #inscrever_criado.delay(inscrever.id)
            request.session['inscrever_id'] = inscrever.id # redirect to the payment
        return redirect(reverse('payment:process'))
            #return render(request,'inscrever/inscrever.html')
    context = {'form': form}
    return render(request,'inscrever/inscrever.html',context)
