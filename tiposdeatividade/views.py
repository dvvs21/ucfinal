from django.shortcuts import render

# Create your views here.

def index (requirements):
    return render(requirements, index.html)
    