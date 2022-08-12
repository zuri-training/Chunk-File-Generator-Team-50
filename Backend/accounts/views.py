from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


    #login user view
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('main:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('split_file:split_home')
            else:
                messages.info(request, "Password or email is incorrect")
                
        return render(request, 'accounts/signin.html')
    
    #log-out view
def logoutUser(request):
    logout(request)
    return redirect('accounts:login')

    #register-user view
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('main:index')
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('split_file:split_home')
            else:
                messages.error(request, "Error in registering user:")
                
        context = {'form':form}
        return render(request, 'accounts/signup.html', context)

def dashboard(request):
    return render(request, 'accounts/profile_screen.html')
