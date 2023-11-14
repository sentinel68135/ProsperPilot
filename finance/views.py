from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AccountForm
from finance.models import Account, Transaction



def dashboard_view(request):
    accounts = Account.objects.filter(user=request.user.id)
    context = {
            'accounts': accounts,
        }
    return render(request, 'dashboard.html', context)

def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created! Cheers')
            return redirect('dashboard')
        else:
            messages.error(request, 'This site sucks!')
            print(form.errors)
    else:
        form = AccountForm()


    return render(request, "create_account.html", {'form':form})