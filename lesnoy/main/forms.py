from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Complaints

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control", "id": f"form_{field}"})

    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()

class UserAuthentificationForm(AuthenticationForm):
    class Meta:
        model = User
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control", "id": f"form_{field}"})


class ComplaintForm(forms.Form):
    title = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "form_title"})
    )
    house_address = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "form_house_address"})
    )
    text = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "id": "form_text",
            "style": "resize: none; text-align: justify; height: 250px;"
        })
    )

    def clean_title(self):
        data = self.cleaned_data["title"]

        if len(data) > 3:
            raise ValidationError("Количество символов превышает максимальное (40)")
        
        return data

class SendMessageForm(forms.Form):
    title = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "form_title"})
    )
    text = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "id": "form_text",
            "style": "resize: none; text-align: justify; height: 250px;"
        })
    )

class SendReplyForm(forms.Form):
    text = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "id": "form_text",
            "style": "resize: none; text-align: justify; height: 250px;"
        })
    )

class SendMeterReadingsForm(forms.Form):
    personal_account = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "form_pa"})
    )
    cold_watter_supply = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control", "id": "form_cws"})
    )
    hot_watter_supply = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control", "id": "form_hws"})
    )
    gas_supply = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control", "id": "form_gs"})
    )
    electricity_supply = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control", "id": "form_es"})
    )
