from django.contrib import admin

from auths.models.my_user import (
    MyUserManager,
    MyUser,
    Transaction,
)
from auths.models.bank_card import BankCard
from auths.models.activation_code import ActivationCode

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'email',
        'nickname',
        'currency',
    )
    list_filter: list[str] = (
        'nickname',
    ) 


@admin.register(ActivationCode)
class CodeAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'code',
        'datetime_created'
    )
    list_filter: list[str] = (
        'user',
    )



@admin.register(BankCard)
class BancCardAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'number',
        'owner',
        'experation_time',
        'cvv'
    )
    list_filter: list[str] = (
        'owner',
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'amount',
        'datetime_created',
        'is_filled',
    )
    list_filter: list[str] = (
        'user',
    )