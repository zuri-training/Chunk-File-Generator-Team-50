from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="accounts:login")
def split_home(request):
    return render(request, 'split_home.html')
def split_csv(request):
    return render(request, 'split_file/split_csv.html')
def split_json(request):
    return render(request, 'split_file/split_json.html')