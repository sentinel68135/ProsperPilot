from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_type', 'name', 'balance']
        widgets = {
            'account_type': forms.Select(choices=Account.ACCOUNT_TYPE_CHOICES)
        }