from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class DateForm(forms.Form):
    start = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control form-control-sm w-auto"}
        )
    )
    end = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control form-control-sm w-auto"}
        )
    )
