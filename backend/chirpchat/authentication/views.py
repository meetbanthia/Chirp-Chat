from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = ''
    return render(request, 'authentication/login.html', {'error_message': error_message})

def home(request):
    return render(request,'authentication/base.html')


def logout_view(request):
    return HttpResponse('''<a href="http://127.0.0.1:8000">Logout</a>''')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # replace 'home' with the name of your home page URL pattern
    else:
        form = UserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})


