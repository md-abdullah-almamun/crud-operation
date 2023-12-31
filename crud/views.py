from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile

# Create your views here.

def First(request):
    user_prof = Profile.objects.all()
    print(user_prof)

    return render(request, 'first/First.html', locals())


def Create(request):
    name = request.POST.get('name')
    image = request.FILES.get('image')
    email = request.POST.get('email')
    age = request.POST.get('age')
    address = request.POST.get('address')
    phone_no = request.POST.get('Phone_no')
    date_of_birth = request.POST.get('date_of_birth')
    religion = request.POST.get('religion')
    gender = request.POST.get('gender')
    if name:
        if image:
            prof = Profile.objects.create(
                name = name,
                image = image,
                Email = email,
                age = age,
                address = address,
                phone_no =phone_no,
                date_of_birth =date_of_birth,
                religion=religion,
                gender=gender,
            )
            prof.save()
            messages.success(request,"profile Derails Created")
            return redirect('first')
        else:
            prof = Profile.objects.create(
                name=name,
                Email=email,
                age=age,
                address=address,
                phone_no=phone_no,
                date_of_birth=date_of_birth,
                religion=religion,
                gender=gender,
            )

            prof.save()
            messages.success(request, "profile Derails Created")
            return redirect('first')


    return render(request, 'First/create.html', locals())
