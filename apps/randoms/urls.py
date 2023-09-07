''' RANDOMS URLS'''
from django.urls import path

from randoms.views.base_view import BaseView
from randoms.views.random_view import RandomView
from randoms.views.slot_machine import SlotMachineView
from randoms.views.bet_view import BetView


urlpatterns = [
    path('slot_mashine/', SlotMachineView.as_view()),
    path('wheel/', RandomView.as_view(), name='random'),
    path('bet/', BetView.as_view()),
    path('', BaseView.as_view())
]



