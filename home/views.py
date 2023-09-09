from django.shortcuts import render



def home(request):
    return render(request, 'home/home.html')


def register(request):
    return render(request, 'registration/register.html')
