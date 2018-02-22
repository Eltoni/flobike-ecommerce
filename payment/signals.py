from django.shortcuts import render,reverse,get_object_or_404
from django.conf import settings
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order
from inscrever.models import Inscrever

def payment_notification (sender,**kwargs):
    ipn_obj=sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        #payment was successful
        if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
            # Not a valid payment
            return
        order = get_object_or_404(Order,id=ipn_obj.invoce)
        order.pago = True
        order.save()
valid_ipn_received.connect(payment_notification)
