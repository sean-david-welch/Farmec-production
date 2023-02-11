# Create your views here.
import os
import json
import stripe
import stripe.error
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from . models import StripeProduct, PaymentProduct

# Create your views here.
stripe.api_key = os.environ.get('TEST_SECRET_KEY')


##############################
####### Stripe Endpoints #####
##############################
def successview(request):
    if request.method == 'POST':
        return redirect('home')
    
    context = {}
    return render(request, 'stripepayments/success.html', context)

def cancelview(request):
    if request.method == 'POST':
        return redirect('payments')
    
    context = {}
    return render(request, 'stripepayments/cancel.html', context)

##############################
####### Stripe Checkout ######
##############################
class PaymentsLandingPageView(TemplateView):
    template_name = 'stripepayments/payments.html'

    def get_context_data(self, **kwargs):
        product = PaymentProduct.objects.get(name='Test Product')
        context = super(PaymentsLandingPageView, self).get_context_data(**kwargs)
        context.update({
            'product': product,
            'TEST_PUBLIC_KEY': os.environ.get('TEST_PUBLIC_KEY'),
        })
        return context

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = PaymentProduct.objects.get(id=product_id)
        YOUR_DOMAIN = os.environ.get('YOUR_DOMAIN')
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'eur',
                            'unit_amount': product.price,
                            'product_data': {
                                'name': product.name,
                            },
                        },
                        'quantity': 1,
                    },
                ],
                metadata={
                    "product_id": product.id
                },
                mode='payment',
                success_url= YOUR_DOMAIN + '/stripepayments/success/',
                cancel_url= YOUR_DOMAIN + '/stripepayments/cancel/',
            )
            if request.method == 'POST':
                return redirect(checkout_session.url, code=303)
            print(JsonResponse({
                'id': checkout_session.id
            }))
        except Exception as e:
            return str(e)
        
    
######################################
####### Stripe Payement Intents ######
######################################
def intentsLandingPage(request):
    product = PaymentProduct.objects.all().first()
    publicKey = os.environ.get('TEST_PUBLIC_KEY')

    context = {'product': product, 'TEST_PUBLIC_KEY': publicKey}
    return render(request, 'stripepayments/checkout.html', context)

class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
            try:
                product_id = self.kwargs['pk']
                product = PaymentProduct.objects.get(id=product_id)

                payment_intent = stripe.PaymentIntent.create(
                    amount=product.price,
                    currency='eur',
                    automatic_payment_methods = {'enabled': True},
                    metadata={
                        "product_id": product.id
                    }
                )
                return JsonResponse({
                    'clientSecret': payment_intent.client_secret
                })
            except Exception as e:
                return JsonResponse({'error': str(e) }) 
         

##############################
####### Stripe Webhooks ######
##############################
endpoint_secret = os.environ.get('WEBHOOK_SECRET')

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    
    if event['type'] == 'checkout.session.completed' or event['type'] == 'payment.intent.created':
        session = event['data']['object']

        customer_email = session['customer_details']['email']
        product_id = session['metadata']['product_id']

        product = PaymentProduct.objects.get(id=product_id)

        send_mail (
            subject = 'Here is your product',
            message = f'Thanks for your purchase, here is the product you ordered, find it here at {product.url}',
            recipient_list= [customer_email],
            from_email= [os.environ.get('EMAIL_HOST_USER')],
        )
    elif event['type'] == 'payment.intent.succeeded' or event['type'] == 'charge.succeeded':
        send_mail (
            subject = '💰💰💰 Payment Received!',
            message = f'You have received a payment of {product.price}',
            recipient_list= [os.environ.get('EMAIL_HOST_USER')],
            from_email= [os.environ.get('EMAIL_HOST_USER')],
        )
    else:
      print('Unhandled event type {}'.format(event['type']))
    
    return HttpResponse(status=200)

