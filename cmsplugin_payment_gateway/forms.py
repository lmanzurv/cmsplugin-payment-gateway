# -*- coding: utf-8 -*-
from django import forms

class PaymentForm(forms.Form):
    payment_method_nonce = forms.CharField()
    payment_value = forms.DecimalField(min_value=0, decimal_places=2)
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField(required=False)
    email = forms.EmailField(required=False)
