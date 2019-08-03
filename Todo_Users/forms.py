from django import forms
from . import models


class UserInfo(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = [
            'username',
            'password'
        ]
