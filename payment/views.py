from django.shortcuts import render,reverse,get_object_or_404

# Create your views here.
from decimal import Decimal
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from inscrever.models import Inscrever
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt


def payment_process(request):
    inscrever_id = request.session.get('inscrever_id')
    inscrever = get_object_or_404(Inscrever, id=inscrever_id)
    host = request.get_host()
    paypal_dict = {'business': settings.PAYPAL_RECEIVER_EMAIL,
                    'amount': '%.2f' % inscrever.valor.quantize(Decimal('.01')),
                    'item_name': 'Inscrever {}'.format(inscrever.id),
                    'invoice': str(inscrever.id),
                    'currency_code': 'BRL',
                    'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
                    'return_url': 'http://{}{}'.format(host,reverse('payment:done')),
                    'cancel_return': 'http://{}{}'.format(host,reverse('payment:cancelado')),
                    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'inscrever': inscrever, 'form':form}
    return render(request,'payment/process.html',context)

@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')
@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/cancelado.html')


def payment_process_order(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()
    paypal_dict = {'business': settings.PAYPAL_RECEIVER_EMAIL,
                    'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
                    'item_name': 'Order {}'.format(order.id),
                    'invoice': str(order.id),
                    'currency_code': 'BRL',
                    'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
                    'return_url': 'http://{}{}'.format(host,reverse('payment:done')),
                    'cancel_return': 'http://{}{}'.format(host,reverse('payment:cancelado')),
                    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'order': order, 'form':form}
    return render(request,'payment/process.html',context)
