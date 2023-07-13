from django.shortcuts import render

def home(request):
    return render(request, 'apps/home.html', {})

def about(request):
    return render(request, 'apps/about.html', {})
