<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
]
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.CustomUserRegistrationView.as_view(), name='register'),
    path('login/', views.CustomUserLoginView.as_view(), name='login'),
    path('logout/', views.CustomUserLogoutView.as_view(), name='logout'),
]
>>>>>>> 7a78d1f2bc5269e6dfb8c4ba1e1c7ed4dc78737f
