from django import forms
from django.core.exceptions import ValidationError
from account.models import User

class LoginForm(forms.Form):
    username = forms.CharField(min_length=2)
    password = forms.CharField(min_length=2)

class SignupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField()
    short_description = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력한 사용자명({username})은 이미 사용중입니다")
        return username