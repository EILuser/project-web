from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserAuthentificationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import ComplaintForm
from . import models
from django.contrib.auth.models import User

def main(request):
    return render(request, "index.html")

def all_complaints(request):
    comps = models.Complaints.objects.all()
    return render(request, "complaints.html", {"complaints": comps})

def my_complaints(request, user_id):
    user = get_object_or_404(User, id=user_id)
    my_comps = models.Complaints.objects.filter(user_id=user.id)
    return render(request, "my_complaints.html", {"complaints": my_comps})

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

def add_complaint_view(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            table_field = models.Complaints(
                title=form.cleaned_data["title"],
                user_id=user.id,
                house_address=form.cleaned_data["house_address"],
                text=form.cleaned_data["text"]
            )
            table_field.save()
            messages.success(request, "Жалоба отправлена успешно")
            return redirect(f"./{id}")
        messages.error(request, "Отправка формы не удалась. Проверьте правильность заполнения полей")
    else:
        form = ComplaintForm()
    return render(request, "send_complaints.html", {"form": form})