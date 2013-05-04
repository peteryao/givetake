from volunteer.models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout

def index(request):

    return render_to_response('volunteer/index.html', {
        
        }, context_instance=RequestContext(request))