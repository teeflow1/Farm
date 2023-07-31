from django.shortcuts import render
from farm_app.models import Category, Farmer, Product, ProductImage, CartOrder, CartOrderItem, ProductView, wishlist, Address

def home(request):
    products = Product.objects.all()
    
    return render(request, 'apps/home.html', {'products':products})


def index(request):
    return render(request, 'apps/index.html', {})

def about(request):
    return render(request, 'apps/about.html', {})


def service(request):
    return render(request, 'apps/service.html', {})

def product(request):
    return render(request, 'apps/product.html', {})
    
    
def contact(request):
    return render(request, 'apps/contact.html', {})
    




