# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig

class PaymentGatewayConfig(AppConfig):
    name = 'cmsplugin_payment_gateway'

    def ready(self):
        # FIXME Make the Braintree info configurable
        import braintree
        braintree.Configuration.configure(braintree.Environment.Sandbox, merchant_id='2m5fg96smvrs6tft', public_key='dhh8fn7bh94kn7qd',
            private_key='a9b546bdc6a817984802205178666970')
