from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account')
    else:
        form = UserCreationForm()
    return render(request, 'customers/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('account')
    else:
        form = AuthenticationForm()
    return render(request, 'customers/login.html', {'form': form})

@login_required
def account_view(request):
    return render(request, 'customers/account.html')

def logout_view(request):
    logout(request)
    return redirect('homepage')
