# ЛБ №5–6 — UI у Django та Flask

Два незалежні застосунки з однаковою предметною областю: реєстрація на навчальні події.

## Структура
- `django_project/` — Django, DTL, Django Forms, messages, CSRF.
- `flask_project/` — Flask, Jinja2, Flask-WTF, flash, CSRF.

## Вимоги
Python 3.12+ (рекомендовано окремі віртуальні середовища для кожного проєкту).

## Запуск Django (Windows, PowerShell)
```powershell
cd django_project
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Відкрити http://127.0.0.1:8000/

## Запуск Flask (окремий термінал)
```powershell
cd flask_project
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```
Відкрити http://127.0.0.1:5000/

Для реального розгортання встановити власний секретний ключ у змінній середовища `FLASK_SECRET_KEY`. У навчальному режимі застосунок має тимчасовий ключ за замовчуванням.

## Перевірка
1. Відкрий головну сторінку та сторінку подій.
2. Надішли форму реєстрації з коректними даними.
3. Перевір помилки: коротке ім'я, неправильний email, порожній тип події або повідомлення менш ніж із 5 слів.
4. Перевір CSRF: у браузері відкрий Developer Tools → Network, надішли форму, переглянь POST-запит і переконайся, що він містить CSRF-поле. Для перевірки відмови без токена можна виконати POST без CSRF-cookie/поля:
   - Django: `curl -i -X POST http://127.0.0.1:8000/register/`
   - Flask: `curl -i -X POST http://127.0.0.1:5000/register`
   Очікується відмова (403 або відповідь із помилкою CSRF). Не вимикайте CSRF для цієї перевірки.

## Примітка
Дані демонстраційних подій передаються з view/route у шаблони. Реєстраційні форми демонструють серверну валідацію; записи не зберігаються в БД, оскільки завдання зосереджене на шаблонах і формах.
