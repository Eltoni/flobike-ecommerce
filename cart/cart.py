from decimal import Decimal
from django.conf import settings
from loja.models import Produto
class Cart(object):
    def __init__(self,resquest):
        """ Inicializa o Carrinho """
        self.session = resquest.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #salva em vazio a session no Carrinho
            cart =self.session[settings.CART_SESSION_ID]={}
        self.cart = cart
    def add(self,produto,quantidade=1,update_quantidade = False):
        """
        Adicionar um produto no carrinho ou atualizar sua quantidade
        """
        produto_id = str(produto.id)
        if produto_id not in self.cart:
            self.cart[produto_id] = {'quantidade':0,'preco':str(produto.preco)}
        if update_quantidade:
            self.cart[produto_id]['quantidade'] = quantidade
        else:
            self.cart[produto_id]['quantidade'] += quantidade
        self.save()
    def save(self):
        #atualiza a session do Carrinho
        self.session[settings.CART_SESSION_ID] = self.cart
        #Marca a session como modificado  para garantir que ela seja salva
        self.session.modified = True


    def remove(self, produto):
        """
        Remove a product from the cart.
        """
        produto_id = str(produto.id)

        if produto_id in self.cart:
            del self.cart[produto_id]
            self.save()

    def __iter__(self):
        """
        Iterate sobre os itens no carrinho e obter os produtos
        do banco de dados.
        """
        produto_ids = self.cart.keys()
        # get the product objects and add them to the cart
        produtos = Produto.objects.filter(id__in=produto_ids)
        for produto in produtos:
            self.cart[str(produto.id)]['produto'] = produto

        for item in self.cart.values():
            item['preco'] = Decimal(item['preco'])
            item['total_preco'] = item['preco'] * item['quantidade']
            yield item
    def __len__(self):
        """
        Conta todos item no carrinho.
        """
        return sum(item['quantidade'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['preco']) * item['quantidade'] for item in
    self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
