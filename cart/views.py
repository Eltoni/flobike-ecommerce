from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_POST
from loja.models import Produto
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, produto_id):
    cart = Cart(request)
    produto = get_object_or_404(Produto, id=produto_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(produto=produto,quantidade=cd['quantidade'],update_quantidade=cd['update'])
    return redirect('cart:cart_detalhes')
def cart_remove(request,produto_id):
    cart = Cart(request)
    produto = get_object_or_404(Produto, id=produto_id)
    cart.remove(produto)
    return redirect('cart:cart_detalhes')
def cart_detalhes(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantidade':item['quantidade'],'update': True})
    return render(request, 'cart/detalhes.html', {'cart': cart})
