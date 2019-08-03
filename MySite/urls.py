from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Todo.urls')),
    path('login/', include('Todo_Users.urls')),
]
