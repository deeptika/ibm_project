from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def home(request):
    user = UserForm()
    return render(request,'sentiment_analyser/home.html', {'form':user})



