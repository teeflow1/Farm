from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm 


def register_user(request): 
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have been logged in succcessfully!!"))
            return redirect('login')
        
    return render(request, 'auth/register_user.html', {'form':form})


def login_user(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully Logged in!!")
            return redirect('home')
        
        else:
            messages.success(request, "There is an Error in your form, Try Again!!!")
            return redirect('login')
    
    
    else:
        return render(request, 'auth/login_user.html', {})
    
    
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out succesfully!!')
    return redirect('home')
    