from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="accounts:login")
def home(request):
    return render(request, "main/home.html")

def documentation(request):
    return render(request, "main/documentation.html")
def features(request):
    return render(request, 'main/features.html')