from django.db import models
from django.conf import settings


class Account(models.Model):

    ACCOUNT_TYPE_CHOICES = (
        ('savings', 'Savings'),
        ('credit_card', 'Credit Card'),
        ('checking', 'Checking'),
    )
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SavingsAccount(Account):
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)

class CreditCardAccount(Account):
    credit_limit = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50, default='Checking')
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"Transaction on {self.account}: {self.amount} {self.transaction_type}"

