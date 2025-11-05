from django import forms
from .models import Pokemon
from .models import Trainer

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels = {
            'name': "Nombre:",
            'type': "Tipo:",
            'weight': "Peso:",
            'height': "Altura:",
            'picture' : "Fotografia",
            'trainer': "Entrenador:"
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}), 
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}),
            'trainer': forms.Select(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"})
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        labels = {
            'name': "Nombre:",
            'last_name': "Apellido:",
            'level': "Nivel:",
            'birth': "Fecha de nacimiento:",
            'picture' : "Fotografia",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}),
            'level': forms.NumberInput(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}),
            'birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}), 
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}),
        }
        