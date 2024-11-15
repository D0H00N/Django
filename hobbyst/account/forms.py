from django import forms
from account.models import User
from django.core.exceptions import ValidationError

# from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=2,
        widget=forms.TextInput(attrs={"placeholder": "사용자명 (2자리 이상)"}),
    )
    password = forms.CharField(
        min_length=2,
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호 (2자리 이상)"}),
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        min_length=2,
        widget=forms.TextInput(attrs={"placeholder": "사용자명 (2자리 이상)"}),
    )
    password1 = forms.CharField(
        min_length=2,
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호 (2자리 이상)"}),
    )
    password2 = forms.CharField(
        min_length=2,
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호 (2자리 이상)"}),
    )
    profile_image = forms.ImageField(required=False)
    preference = forms.MultipleChoiceField(
        choices=User.preference_choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    short_description = forms.CharField()

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "profile_image",
            "preference",
            "short_description",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["preference"].label = "선호하는 취미 카테고리 (복수 선택 가능)"

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력한 사용자명 ({username})은 이미 사용 중입니다.")
        return username

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            self.add_error("password2", "비밀번호와 비밀번호 확인란의 값이 다릅니다.")

    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        profile_image = self.cleaned_data["profile_image"]
        preference = self.cleaned_data["preference"]
        short_description = self.cleaned_data["short_description"]
        user = User.objects.create_user(
            username=username,
            password=password1,
            profile_image=profile_image,
            preference=preference,
            short_description=short_description,
        )
        return user
