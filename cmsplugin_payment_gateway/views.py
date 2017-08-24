# -*- coding: utf-8 -*-
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from .forms import PaymentForm
import braintree

def make_payment(request):
    if request.method == 'GET':
        return render(request, 'payment_form.html', {'client_token': braintree.ClientToken.generate()})
    elif request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # FIXME Store the transaction result somewhere to query
            # FIXME Make the merchant_account_id configurable
            payment_value = form.cleaned_data['payment_value']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            data = {
                'amount': payment_value,
                'payment_method_nonce': form.cleaned_data['payment_method_nonce'],
                'merchant_account_id': '1234512346',
                'customer': {
                    'first_name': first_name,
                    'last_name': last_name
                },
                'options': {
                    'submit_for_settlement': True
                }
            }
            phone = form.cleaned_data.get('phone')
            if phone:
                data['customer']['phone'] = phone
            email = form.cleaned_data.get('email')
            if email:
                data['customer']['email'] = email
            result = braintree.Transaction.sale(data)
            if result.is_success:
                return render(request, 'thank_you.html')
            else:
                messages.error(request, 'The payment was rejected. Please try again')
                return render(request, 'payment_form.html', {'client_token': braintree.ClientToken.generate(), 'first_name': first_name,
                    'last_name': last_name, 'payment_value': payment_value, 'phone': phone, 'email': email})
        else:
            messages.error(request, 'Invalid payment details')
            return render(request, 'payment_form.html', {'client_token': braintree.ClientToken.generate()})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
