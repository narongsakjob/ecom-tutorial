# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    publish_key = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = request.user.userstripe.stripe_id
    # if (request.method == 'POST'):
    #     print(request.POST)
    #     token = request.POST['stripeToken']
    #     try:
    #         customer = stripe.Customer.retrieve(customer_id)
    #         customer.sources.create(source=token)
    #         charge = stripe.Charge.create(
    #             amount=1000,
    #             currency="usd",
    #             customer=customer,
    #             description="Example charge"
    #         )
    #     except stripe.error.CardError as e:
    #         pass
    context = {
        'publish_key': publish_key
    }
    return render(request, 'checkout.html', context)
