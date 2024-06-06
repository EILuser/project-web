from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.items():
            field[1].widget.attrs.update({"class": "form-control", "id": f"form_{field[0]}"})

    first_name = forms.CharField(
        max_length=20,
        validators= [
            RegexValidator(
                regex=r"^[А-Яа-я]{3,20}$",
                message="Введите корректное имя"
            )
        ]
    )
    last_name = forms.CharField(
        max_length=20,
        validators= [
            RegexValidator(
                regex=r"^[А-Яа-я]{3,20}$",
                message="Введите корректную фамилию"
            )
        ]
    )
    email = forms.EmailField()

class UserAuthentificationForm(AuthenticationForm):
    class Meta:
        model = User
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.items():
            field[1].widget.attrs.update({"class": "form-control", "id": f"form_{field[0]}"})


class ComplaintForm(forms.Form):
    title = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "form_title"}),
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

    # Валидация формы
    def clean_title(self):
        data = self.cleaned_data["title"]

        if len(data) > 40:
            raise ValidationError("Количество символов превышает максимальное (40)")
        
        return data
    
    def clean_house_address(self):
        data = self.cleaned_data["house_address"]

        if len(data) > 40:
            raise ValidationError("Количество символов превышает максимальное (40)")
        
        return data
    
    def clean_text(self):
        data = self.cleaned_data["text"]

        if len(data) > 1000:
            raise ValidationError("Количество символов превышает максимальное (1000)")
        
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

    def clean_text(self):
        data = self.cleaned_data["text"]

        if len(data) > 1000:
            raise ValidationError("Превышен лимит в 1000 символов")

        return data

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
