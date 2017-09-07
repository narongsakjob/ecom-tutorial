# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	context = locals()
	return render(request, 'home.html', context)

def about(request):
	context = locals()
	return render(request, 'about.html', context)

@login_required
def userProfile(request):
	user = request.user
	context = { 'user': user }
	return render(request, 'profile.html', context)