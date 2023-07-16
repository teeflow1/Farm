from django.shortcuts import render
from farm_app.models import Category, Farmer, Product, ProductImage, CartOrder, CartOrderItem, ProductView, wishlist, Address

def home(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    
    return render(request, 'apps/home.html', context)

def about(request):
    return render(request, 'apps/about.html', {})
