from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import CustomUser


class CustomUserRegistrationView(CreateView):
    model = CustomUser
    template_name = 'registration/register.html'
    fields = ('username', 'email', 'password')
    success_url = reverse_lazy('login')


class CustomUserLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomUserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


def home(request):
    return render(request, 'home.html')
