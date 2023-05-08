from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as dj_login, logout as dj_logout, authenticate
from django.contrib.auth.models import User


class HomePage(TemplateView):
    template_name = 'main/index.html'

#def index(request):
 #   return render(request, "main/index.html")

def training(request):
    return render(request, "main/training.html")

def practice(request):
    return render(request, "main/practice.html")  

def registration(request):
    if request.method == "GET":
        return render(request, "main/registration.html", {'form': UserCreationForm()})  
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                dj_login(request, user)
                return redirect('home')
            except IntegrityError:
                 return render(request, "main/registration.html", {'form': UserCreationForm(), 'error': 'Пользователь с таким именем уже существует'})

        else:
            return render(request, "main/registration.html", {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})
            print('Hello')

def login(request):
    if request.method == "GET":
        return render(request, "main/login.html", {'form': AuthenticationForm()})  
    else:
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password')) 
        if user is None:
            return render(request, "main/login.html", {'form':AuthenticationForm(), 'error': 'Неверный логин или пароль'})
        else:
            dj_login(request, user)
            return redirect('home')

def logout(request):
    if request.method == 'POST':
        dj_logout(request)
        return redirect('home')
    


