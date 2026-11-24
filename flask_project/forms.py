from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError

class RegistrationForm(FlaskForm):
    full_name = StringField(
        "Ім’я та прізвище",
        validators=[DataRequired(message="Заповніть ім’я."), Length(min=2, max=60, message="Ім’я має містити від 2 до 60 символів.")]
    )
    email = EmailField(
        "Електронна пошта",
        validators=[DataRequired(message="Вкажіть email."), Email(message="Введіть коректну адресу email.")]
    )
    event = SelectField(
        "Подія",
        choices=[
            ("python", "Python для початківців"),
            ("security", "Основи кібербезпеки"),
            ("web", "Веброзробка"),
        ],
        validators=[DataRequired(message="Оберіть подію.")]
    )
    message = TextAreaField(
        "Чому бажаєте долучитися?",
        validators=[DataRequired(message="Напишіть повідомлення."), Length(min=1, max=1000, message="Повідомлення не може перевищувати 1000 символів.")]
    )
    submit = SubmitField("Надіслати заявку")

    def validate_full_name(self, field):
        if any(char.isdigit() for char in field.data or ""):
            raise ValidationError("Ім’я не повинно містити цифр.")

    def validate_message(self, field):
        if len((field.data or "").split()) < 5:
            raise ValidationError("Повідомлення має містити щонайменше 5 слів.")
