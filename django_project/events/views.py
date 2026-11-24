from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import RegistrationForm

EVENTS = [
    {"title": "Python для початківців", "seats": 24, "description": "Практичне знайомство з мовою Python та її можливостями."},
    {"title": "Основи кібербезпеки", "seats": 18, "description": "Базові принципи захисту інформації та безпечної поведінки онлайн."},
    {"title": "Веброзробка", "seats": 12, "description": "Створення сторінок і знайомство з серверною логікою."},
]

def home(request):
    context = {"page_name": "Навчальні події", "events_count": len(EVENTS),
               "events": EVENTS, "year": timezone.now().year}
    return render(request, "events/home.html", context)

def event_list(request):
    context = {"page_name": "Каталог подій", "events_count": len(EVENTS),
               "events": EVENTS, "year": timezone.now().year}
    return render(request, "events/events.html", context)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, f"Дякуємо, {form.cleaned_data['full_name']}! Заявку прийнято.")
            return redirect("register")
        messages.error(request, "Перевірте поля форми та виправте помилки.")
    else:
        form = RegistrationForm()
    return render(request, "events/register.html", {"form": form, "year": timezone.now().year})
