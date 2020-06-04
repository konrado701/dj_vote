from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser, Glosowanie, Kandydat

class CreateUseForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'wiek', 'woj', 'wyk']

class CreateGlosowanie(ModelForm):
    class Meta:
        model = Glosowanie
        fields = ['nazwa', 'czas_glosowania', 'ilosc_mozliwych_kandydatow']

class CreateKandydat(ModelForm):
    class Meta:
        model = Kandydat
        fields = ['imie', 'nazwisko']