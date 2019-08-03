from django.shortcuts import render
from . import forms
from . models import UserProfile


# Create your views here.

def sign_in(request):
    if request.method == "POST":
        form = forms.UserInfo(request.POST or None)

        if form.is_valid():
            user_info = UserProfile.objects.all()
            for user in user_info:
                if user in user_info:
                    return render(request, 'app-templates/home.html', {
                        'user_info': user_info
                    })
                else:
                    form.save()
                    user_info = UserProfile.objects.all()
                    return render(request, 'app-templates/home.html', {
                        'user_info': user_info
            })

    else:
        return render(request, 'app-templates/loginpage.html', {})


def homepage(request):
    return render(request, 'app-templates/loginpage.html', {})


