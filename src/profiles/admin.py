# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import profile

# Register your models here.
class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = profile

admin.site.register(profile, profileAdmin)