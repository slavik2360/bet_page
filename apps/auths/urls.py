
''' AUTHS URLS'''

from django.contrib import admin
from django.urls import path

from auths.views import (
    RegisterView,
    LoginView
)

urlpatterns = [
    path('reg/', RegisterView.as_view()),
    path('log/', LoginView.as_view())
]
