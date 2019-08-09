from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import List
from . forms import ListForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request, 'todo_temps/homepage.html', {})


def todo_home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, 'Item has been added to the list!')
            return render(request, 'todo_temps/home.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'todo_temps/home.html', {'all_items': all_items})


def delete(request, list_id):
    List.objects.get(pk=list_id).delete()
    messages.success(request, 'Item has been deleted!!!')
    return redirect('home')


def crossed(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    messages.success(request, 'Item has been crossed!!!')
    return redirect('home')


def un_crossed(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    messages.success(request, 'Item has been crossed!!!')
    return redirect('home')


def edit(request, list_id):
    if request.method == "POST":
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Item has been edited!!!')
            return redirect('home')

    else:
        all_items = List.objects.get(pk=list_id)
        return render(request, 'todo_temps/edit.html', {'all_items': all_items})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'todo_temps/register.html', {'form': form})


def login_page(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("You are now logged in !!!")
        else:
            return redirect('login')

    return render(request, 'todo_temps/login.html')
