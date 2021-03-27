from django.shortcuts import render
from .forms import LoginForm, RegisterForm

def index(request):
    form = LoginForm()
    context = {
            'form':form
            }
    return render(request, 'login.html', context)

def register(request):
    form = RegisterForm()
    context = {
            'form':form
            }
    return render(request, 'register.html', context)

# Create your views here.
