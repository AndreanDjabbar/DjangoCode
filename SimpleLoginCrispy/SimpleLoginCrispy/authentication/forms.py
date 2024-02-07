from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
            "class":"form-control",
            "placeholder":"Input Email"
        }
        )
    )
    is_agree = forms.BooleanField(
        required=True,
    )
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Input Username"
        self.fields["password1"].widget.attrs["placeholder"] = "Input Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Input Password Confirmation"

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Input Username"
            }
        )
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Input Password"
            }
        )
    )
