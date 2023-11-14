from django.contrib import admin
from .models import SavingsAccount, CreditCardAccount, Transaction

admin.site.register(SavingsAccount)
admin.site.register(CreditCardAccount)
#admin.site.register(CheckingAccount)
admin.site.register(Transaction)
