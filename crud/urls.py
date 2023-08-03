from django.urls import path
from .views import *

urlpatterns = [
    path('', First, name='first'),
    path('create/', Create, name='create'),



]
