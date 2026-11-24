from django import forms

EVENT_CHOICES = [
    ("python", "Python для початківців"),
    ("security", "Основи кібербезпеки"),
    ("web", "Веброзробка"),
]

class RegistrationForm(forms.Form):
    full_name = forms.CharField(
        label="Ім’я та прізвище", min_length=2, max_length=60,
        widget=forms.TextInput(attrs={"placeholder": "Наприклад, Олена Петренко", "class": "field"})
    )
    email = forms.EmailField(
        label="Електронна пошта",
        widget=forms.EmailInput(attrs={"placeholder": "name@example.com", "class": "field"})
    )
    event = forms.ChoiceField(
        label="Подія", choices=EVENT_CHOICES,
        widget=forms.Select(attrs={"class": "field"})
    )
    message = forms.CharField(
        label="Чому бажаєте долучитися?",
        widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Напишіть щонайменше п’ять слів", "class": "field"})
    )

    def clean_full_name(self):
        value = self.cleaned_data["full_name"].strip()
        if any(char.isdigit() for char in value):
            raise forms.ValidationError("Ім’я не повинно містити цифр.")
        return value

    def clean_message(self):
        value = self.cleaned_data["message"].strip()
        if len(value.split()) < 5:
            raise forms.ValidationError("Повідомлення має містити щонайменше 5 слів.")
        return value
