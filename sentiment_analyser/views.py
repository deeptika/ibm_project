from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def home(request):
    return render(request,'sentiment_analyser/home.html')

def form(request):
    user = UserForm()
    return render(request, 'sentiment_analyser/form.html', {'form':user})
