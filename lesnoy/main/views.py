from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserAuthentificationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def main(request):
    return render(request, "index.html")

def home(request):
    return render(request, "test1.html")

def home1(request):
    return render(request, "test2.html")

def home2(request):
    return render(request, "test3.html")

def login_view(request):
    if request.method == "POST":
        form = UserAuthentificationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("..")
        messages.error(request, "Неправильное имя пользователя или пароль")
    else:
        form = UserAuthentificationForm()
    return render(request, "login.html", {"form": form})

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно. Сейчас вы можете войти в аккаунт")
            return redirect("../login")
        messages.error(request, "Регистрация не удалась. Проверьте правильность заполнения полей")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})