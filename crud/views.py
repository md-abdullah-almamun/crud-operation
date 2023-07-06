from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def First(request):
    return render(request, 'First/First.html')

