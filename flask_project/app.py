import os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "dev-only-change-this-key")

csrf = CSRFProtect(app)

EVENTS = [
    {"title": "Python для початківців", "seats": 24, "description": "Практичне знайомство з мовою Python та її можливостями."},
    {"title": "Основи кібербезпеки", "seats": 18, "description": "Базові принципи захисту інформації та безпечної поведінки онлайн."},
    {"title": "Веброзробка", "seats": 12, "description": "Створення сторінок і знайомство з серверною логікою."},
]

@app.context_processor
def inject_year():
    return {"year": datetime.now().year}

@app.route("/")
def home():
    return render_template("home.html", page_name="Навчальні події",
                           events_count=len(EVENTS), events=EVENTS)

@app.route("/events")
def event_list():
    return render_template("events.html", page_name="Каталог подій",
                           events_count=len(EVENTS), events=EVENTS)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Дякуємо, {form.full_name.data}! Заявку прийнято.", "success")
        return redirect(url_for("register"))
    if form.is_submitted() and form.errors:
        flash("Перевірте поля форми та виправте помилки.", "error")
    return render_template("register.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
