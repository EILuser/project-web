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
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control", "id": f"form_{field}"})


class ComplaintForm(forms.Form):
    title = forms.CharField(max_length=40,
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    house_address = forms.CharField(max_length=40,
                                    widget=forms.TextInput(attrs={"class": "form-control"}))
    text = forms.CharField(max_length=1000,
                           widget=forms.Textarea(attrs={"class": "form-control", "rows": "10", "style": "resize: none; text-align: justify"}))