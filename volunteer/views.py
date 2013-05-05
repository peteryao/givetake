from volunteer.models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout

from django.conf import settings

def index(request): 

    return render_to_response('volunteer/index.html', {
        
        }, context_instance=RequestContext(request))

def listing(request):
    service_list = Service.objects.filter(available=True)
    context = {'service_list' : service_list}
    return render(request, 'volunteer/listing.html', context)


def charities(request):
    charity_list = Charity.objects.all()
    context = {'charity_list' : charity_list}
    return render(request, 'volunteer/charities.html', context)

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
            # Return a 'disabled account' error message
    else:
        return HttpResponseRedirect('/')
        # Return an 'invalid login' error message.