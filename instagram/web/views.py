from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from users.models import Victim


@login_required(login_url='users:login')
def index(request):
    print(request.user)
    return render(request, 'web/index.html')


def hacker(request):
    context = {
        'victims': Victim.objects.all()
    }
    return render(request, 'web/hacker.html', context)