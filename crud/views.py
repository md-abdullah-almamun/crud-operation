from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def First(request):
    value = request.POST.get('txt')
    print('your data is in value:', value)
    a = value
    return render(request, 'first/First.html', locals())

