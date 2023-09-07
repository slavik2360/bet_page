from django import forms
from django.core.exceptions import ValidationError

from typing import Any, Dict


class RegisterForm(forms.Form):
    email = forms.EmailField(label='Почта', max_length=200)
    nickname = forms.CharField(label="Ваш ник", max_length=100)
    password = forms.CharField(label="Пароль", min_length=6)
    password2 = forms.CharField(label="Повторите", min_length=6)

    def clean_email(self) -> Dict[str, Any]:
        data: str = self.cleaned_data['email']
        if '@gmail' in data:
            raise ValidationError('Лох, Пидр')
        return data
    
    def clean_password2(self) -> Dict[str, Any]:
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise ValidationError('Пароли не свопадают')
        return self.cleaned_data