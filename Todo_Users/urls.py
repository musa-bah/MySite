from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.homepage, name='home'),
    path('', views.sign_in, name='login'),
]
