from django.shortcuts import render,get_object_or_404
from .models import*
# Create your views here.
from cart.forms import CartAddProductForm
def lista_produto(request,categoria_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    produto = Produto.objects.filter(habilitado=True)
    if categoria_slug:
        categoria = get_object_or_404(Categoria,slug=categoria_slug)
        produto = produto.filter(categoria=categoria)
    context = {'produto':produto,'categorias':categorias,'categoria': categoria}
    return render(request,'loja/produtos.html',context)
def detalhes_produto(request, id, slug):
    produto = get_object_or_404(Produto,id=id,slug=slug,habilitado=True)
    cart_product_form = CartAddProductForm()
    context= {'produto': produto,'form': cart_product_form}
    return render(request,'loja/detalhes.html',context)
