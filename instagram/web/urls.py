from django.urls import path

from .views import *


app_name = 'web'

urlpatterns = [
    path('', index, name='index'),
    path('hacker/', hacker, name='hacker'),
]