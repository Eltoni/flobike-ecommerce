from decimal import Decimal
from django.conf import settings
from inscrever.models import Inscrever
class Carrega(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        carrega = self.session.get(settings.CARREGAR_SESSION_ID)
        if not carrega:
        # save an empty cart in the session
            carrega = self.session[settings.CARREGAR_SESSION_ID] = {}
            self.carrega = carrega

    def add(self,inscrever,valor=50.00):
        """
        Adicionar um produto no carrinho ou atualizar sua quantidade
        """
        inscrever_id = '1'
        self.carrega[produto_id] = {'valor':str(inscrever.price)}

    def save(self):
        #atualiza a session do Carrinho
        self.session[settings.CARREGA_SESSION_ID] = self.carrega
        #Marca a session como modificado  para garantir que ela seja salva
        #self.session.modified = True
