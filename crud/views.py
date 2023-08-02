from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile


# Create your views here.

def First(request):
    user_prof = Profile.objects.all()
    print(user_prof)

    return render(request, 'first/First.html', locals())
