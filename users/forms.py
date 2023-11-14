from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Введите ваше имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Введите вашу фамилию')
    date_of_birth = forms.DateField(required=True, help_text='Введите дату рождения')
    city = forms.CharField(required=False, help_text='Введите город')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'date_of_birth',
            'city',
            'password1',
            'password2',
        ]
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'date_of_birth': 'Дата рождения',
            'city': 'Город',
        }


class EditProfileForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=30, required=False, help_text='Введите ваше имя')
    last_name = forms.CharField(label='Фамилия', max_length=30, required=False, help_text='Введите вашу фамилию')
    date_of_birth = forms.DateField(label='Дата рождения', required=True, help_text='Введите дату рождения')
    city = forms.CharField(label='Город', required=False, help_text='Введите город')