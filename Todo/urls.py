from django.urls import path
from . import views
from django.contrib.auth import authenticate, login

urlpatterns = [
    path('home/', views.todo_home, name='home'),
    path('delete/<int:list_id>', views.delete, name='delete'),
    path('cross/<int:list_id>', views.crossed, name='cross'),
    path('un_cross/<int:list_id>', views.un_crossed, name='un_cross'),
    path('edit/<int:list_id>', views.edit, name='edit'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('', views.home, name='homepage'),

]
