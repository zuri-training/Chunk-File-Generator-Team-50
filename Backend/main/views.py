from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "main/index.html")

def AboutUs(request):
    return render(request, "main/about.html")

def FaQ(request):
    return render(request, "main/faq.html")

def documentation(request):
    return render(request, "main/documentation.html")

def policy(request):
    return render(request, "main/privacypolicy.html")