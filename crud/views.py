from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def First(request):
    value = request.GET.get('txt')
    print(value)
    return render(request, 'first/First.html')

