from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, "authenticate/home.html", {})


#Creating the login form function 
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, (' You have successfully logged in!!!'))
            return redirect('home')
        else:
            messages.success(request, (' Error! logging in ........'))
            return redirect('login')
    else:
        return render(request, "authenticate/login.html", {})


#Creating the logout function 
def logout_user(request):
    logout(request)
    messages.success(request, (' You have been logged out..'))
    return redirect('home')


#Creating the register function 
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, (' You have been logged out..'))
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, "authenticate/register.html", context)

