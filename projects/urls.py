from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from projects.views import hello_world, AccountCreateView

app_name = 'projects'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('create/', AccountCreateView.as_view(), name='create')
]