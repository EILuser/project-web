from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control", "id": f"form_{field}"})

    email = forms.EmailField()

class UserAuthentificationForm(AuthenticationForm):
    class Meta:
        model = User
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control", "id": "form_username"})
        self.fields["password"].widget.attrs.update({"class": "form-control", "id": "form_password"})

    required_css_class = "form-floating"
