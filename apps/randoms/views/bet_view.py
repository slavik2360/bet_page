'''BET VIEWS'''
from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse


from auths.models.my_user import MyUser
from randoms.forms.bet_form import BetForm
from randoms.models.bet import Bet

class BetView(View):

    template_name = 'random/bet.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = BetForm()
        return render(
            template_name=self.template_name,
            request=request,
            context = {
                'form': form,
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        form = BetForm(request.POST)
        us = request.user.id
        user = MyUser.objects.get(pk=us)
        print(user)
        print(form.data)
        if form.is_valid():
            game = form.cleaned_data['game']
            amount = form.cleaned_data['amount']
            coef = form.cleaned_data['coef']

            bet = Bet.objects.create(
                game=game,
                amount=amount,
                who=user,
                coef=coef
            )
            bet.save()
            return HttpResponse('Bet good!')
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form' : form
            }
            )