'''AUTHS VIEWS'''
#Django
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth import get_user_model

#local
from auths.forms.registeg_form import RegisterForm
from auths.forms.login_form import LoginForm
from auths.models.my_user import MyUser

# Create your views here.

class LoginView(View):
    """
    User login.
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        ...

    def post(self, request: HttpRequest) -> HttpResponse:
        ...


class RegisterView(View):
    """
    User Register.
    """
    template_name = 'register.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form' : form
            }
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            us = MyUser.objects.create(**form.cleaned_data)
            us.save()
            return HttpResponseRedirect('/auth/log')
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form' : form
            }
            )



class LoginView(View):
    template_name = 'login.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(
                request=request,
                template_name=self.template_name,
                context={
                    'form' : form
                }
            )
        email = form.cleaned_data['email']
        print(email)
        password = form.cleaned_data['password']
        user: MyUser = authenticate(request, email=email, password=password)
        print(user)
        if not user:
            return render(
                request=request,
                template_name=self.template_name,
                context={
                    'form' : form
                }
            )

        a=login(request, user)
        print(a)

        return redirect('https://www.youtube.com/')



