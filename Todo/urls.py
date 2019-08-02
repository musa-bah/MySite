from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('your-name/', views.home_view),
    path('delete/<int:list_id>', views.delete, name='delete'),
    path('cross/<int:list_id>', views.crossed, name='cross'),
    path('un_cross/<int:list_id>', views.un_crossed, name='un_cross'),
    path('edit/<int:list_id>', views.edit, name='edit'),
]
