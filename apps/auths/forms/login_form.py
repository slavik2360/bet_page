from django import forms
from typing import Any, Dict
from django.core.exceptions import ValidationError
from auths.models.my_user import MyUser


class LoginForm(forms.Form):
    email = forms.EmailField(label='почта', max_length=200)
    password = forms.CharField(label="пароль", min_length=6)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Поле "почта" обязательно для заполнения.')
        return email
    
    class Meta:
        model = MyUser
        fields = {
            'email',
            'password',
        }