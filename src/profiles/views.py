# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
	context = locals()
	return render(request, 'home.html', context)

def about(request):
	context = locals()
	return render(request, 'about.html', context)