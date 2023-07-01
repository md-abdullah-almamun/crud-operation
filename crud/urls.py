from django.urls import path
from .views import *
urlpatterns = [
    path('', First, name='first'),
    path('Secound/',Secound,name='secound'),

]
