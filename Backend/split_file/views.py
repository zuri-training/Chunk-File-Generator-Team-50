from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="accounts:login")
def split_home(request):
    return render(request, 'split_file/home.html')

@login_required(login_url="accounts:login")
def upload_csv(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['csv_file']
        #print uploaded_file size and name
        return redirect('split_file:splitcsv')
    return render(request, 'split_file/uploadcsv.html')

@login_required(login_url="accounts:login")
def split_csv(request):
    if request.method == 'POST':
        return redirect('split_file:downloadcsv')
    return render(request, 'split_file/splitcsv.html')

@login_required(login_url="accounts:login")
def download_csv(request):
    return render(request, 'split_file/downloadcsv.html')

@login_required(login_url="accounts:login")
def save_csv(request):
    if request.method == "POST":
        return redirect('split_file:savedcsvlist')
    return render(request, 'split_file/savecsv.html')

@login_required(login_url="accounts:login")
def saved_csv_list(request):
    return render(request, 'split_file/savedcsvlist.html')

@login_required(login_url="accounts:login")
def split_json(request):
    return render(request, 'split_file/split_json.html')
