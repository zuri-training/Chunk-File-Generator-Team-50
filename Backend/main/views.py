from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def AboutUs(request):
    return render(request, "main/about.html")

def FaQ(request):
    return render(request, "main/faq.html")

def contact(request):
    return render(request, "main/contact_us.html")

def policy(request):
    return render(request, "main/privacypolicy.html")

def terms(request):
    return render(request, "main/termsandconditions.html")
