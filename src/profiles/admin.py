# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile, UserStripe

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = Profile

admin.site.register(Profile, ProfileAdmin)

class UserStripeAdmin(admin.ModelAdmin):
    class meta:
        model = UserStripe

admin.site.register(UserStripe, UserStripeAdmin)