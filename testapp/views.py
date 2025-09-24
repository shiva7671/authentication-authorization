from django.shortcuts import render, redirect
from .models import User
from .decorators import custom_login_required
from django.contrib import messages
# Create your views here.

def nav_view(request):
    return render(request,"navbar.html")

def home_view(request):
    return render(request,"home.html")

@custom_login_required
def transact_view(request):
    return render(request,"transactions.html")

@custom_login_required
def settlement_view(request):
    return render(request,"settlements.html")

@custom_login_required
def account_view(request):
    return render(request,"account.html")

def logout_view(request):
    request.session.flush()
    messages.success(request, "You have been logged out.")
    return redirect('/signin/')


def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('/signup/')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('/signup/')

        User.objects.create(name=name, email=email, password=password)
        messages.success(request, "Account created! Please sign in.")
        return redirect('/signin/')

    return render(request, 'signup.html')


def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email does not exist.")
            return redirect('/signin/')

        if password == user.password:
            request.session['user_id'] = user.id
            messages.success(request, "Signin successful!")
            return redirect('/')  # home page
        else:
            messages.error(request, "Incorrect password.")
            return redirect('/signin/')

    return render(request, 'signin.html')
