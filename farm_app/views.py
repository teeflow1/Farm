from django.shortcuts import render
from farm_app.models import Category, Farmer, Product, ProductImage, CartOrder, CartOrderItem, ProductView, wishlist, Address

def home(request):
    products = Product.objects.all()
    
    return render(request, 'apps/home.html', {'products':products})

def about(request):
    return render(request, 'apps/about.html', {})


def service(request):
    return render(request, 'apps/service.html', {})
    




