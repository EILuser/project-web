from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserRegistrationForm, UserAuthentificationForm, SendMessageForm, ComplaintForm, SendReplyForm, SendMeterReadingsForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . import models
from datetime import datetime

def main_view(request):
    news_list = models.News.objects.all().order_by("-publish_date")[:3]
    unread_messages_count = 0

    if request.user.id is not None:
        if request.user.is_superuser:
            unread_messages_count = models.Messages.objects.filter(
                reply_date__isnull=True,
                is_read=False
            ).count()
        else:
            unread_messages_count = models.Messages.objects.filter(
                user_id=request.user.id,
                reply_date__isnull=False,
                is_read=False).count()
    
    return render(request, "index.html", {"latest_news": news_list, "unread_messages_count": unread_messages_count})

def all_complaints_view(request):
    complaints = models.Complaints.objects.all().order_by("-post_date")
    return render(request, "complaints.html", {"complaints": complaints})

def my_complaints_view(request):
    my_comps = models.Complaints.objects.filter(user_id=request.user.id)
    return render(request, "my_complaints.html", {"complaints": my_comps})

def news_view(request):
    news_list = models.News.objects.all().order_by("-publish_date")
    return render(request, "news.html", {"news": news_list})

def admin_messages_view(request):
    messages = models.Messages.objects.filter(reply_text="Нет ответа").order_by("-send_date")
    return render(request, "admin_messages.html", {"messages_list": messages})

def user_messages_view(request):
    messages = models.Messages.objects.filter(reply_date__isnull=False, user_id=request.user.id).order_by("-reply_date")
    return render(request, "user_messages.html", {"messages_list": messages})

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

def add_complaint_view(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = models.Complaints(
                title=form.cleaned_data["title"],
                user_id=request.user.id,
                house_address=form.cleaned_data["house_address"],
                text=form.cleaned_data["text"],
                post_date=datetime.now().date()
            )
            complaint.save()
            messages.success(request, "Жалоба отправлена успешно")
            return redirect(f"./{request.user_id}")
        messages.error(request, "Отправка формы не удалась. Проверьте правильность заполнения полей")
    else:
        form = ComplaintForm()
    return render(request, "send_complaint.html", {"form": form})

def send_message_view(request):
    if request.method == "POST":
        form = SendMessageForm(request.POST)
        if form.is_valid():
            send_date_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            send_date = datetime.strptime(send_date_string, "%Y-%m-%d %H:%M:%S")
            message = models.Messages(
                user_id=request.user.id,
                send_date=send_date,
                title=form.cleaned_data["title"],
                question_text=form.cleaned_data["text"],
                is_read=False
            )
            message.save()
            messages.success(request, "Сообщение успешно отправлено")
            return redirect(f".")
        messages.error(request, "Сообщение не отправлено. Проверьте правильность заполнения полей")
    else:
        form = SendMessageForm()
    return render(request, "send_message.html", {"form": form})

def make_read_view(request, message_id):
    models.Messages.objects.filter(id=message_id).update(is_read=True)
    return redirect("..")

def delete_message_view(request, message_id):
    models.Messages.objects.filter(id=message_id).delete()
    return redirect("..")

def send_meter_readings_view(request):
    if request.method == "POST":
        form = SendMeterReadingsForm(request.POST)
        if form.is_valid():
            meter_readings = models.MeterReadings(
                user_id=request.user.id,
                send_date=datetime.now().date(),
                personal_account=form.cleaned_data["personal_account"],
                hot_watter_supply=form.cleaned_data["hot_watter_supply"],
                cold_watter_supply=form.cleaned_data["cold_watter_supply"],
                gas_supply=form.cleaned_data["gas_supply"],
                electricity_supply=form.cleaned_data["electricity_supply"]
            )
            meter_readings.save()
            messages.success(request, "Отправка показаний прошла успешно")
            return redirect(".")
        messages.error(request, "Показания не отправились. Проверьте правильность заполнения полей")
    else:
        form = SendMeterReadingsForm()
    return render(request, "send_meterreadings.html", {"form": form})

def reply_view(request, message_id):
    message = models.Messages.objects.filter(id=message_id)
    if request.method == "POST":
        form = SendReplyForm(request.POST)
        if form.is_valid():
            reply_date_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            reply_date = datetime.strptime(reply_date_string, "%Y-%m-%d %H:%M:%S")
            message.update(
                reply_text=form.cleaned_data["text"],
                is_read=False,
                reply_date=reply_date
            )
            messages.success(request, "Ответ отправлен")
            return redirect("..")
    else:
        form = SendReplyForm()
    return render(request, "reply.html", {"messages_list": message, "form": form})