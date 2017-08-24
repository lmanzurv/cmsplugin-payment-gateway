# -*- coding: utf-8 -*-
from django.conf.urls import *  # NOQA
from .views import *

urlpatterns = [
    url(r'^make-payment/$', make_payment, name='make_payment'),
]
