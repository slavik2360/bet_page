from django import forms
from django.core.exceptions import ValidationError

from typing import Any, Dict

from randoms.models.bet import Bet


class BetForm(forms.Form):

    
    GAME_CHOICES = (
        (0, 'Колесо фартуны'),
        (1, 'Игровой Автомат')
    )

    game = forms.ChoiceField(
        label='игра',
        choices=GAME_CHOICES
    )
    amount = forms.DecimalField(
        label='ставка',
        min_value=0,
        max_digits=11,
        decimal_places=2
    )
    # who = forms.CharField(
    #     label="login", 
    #     max_length=100
        
    # )
    coef = forms.DecimalField(
        label='коэф',
        min_value=0,
        max_digits=3,
        decimal_places=1
    )

    # class Meta:
    #     model = Bet
    #     fields = {
    #         'game',
    #         'amount',
    #         'coef',
    #     }