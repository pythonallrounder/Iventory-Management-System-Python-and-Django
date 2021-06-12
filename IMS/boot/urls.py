from django.contrib import admin
from django.urls import path
from boot.views import *
urlpatterns = [
  path('show',show,name='show')
]