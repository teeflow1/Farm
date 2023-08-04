from django.shortcuts import render
from farm_app.models import Category, Farmer, Product, ProductImage, CartOrder, CartOrderItem, ProductView, wishlist, Address
from django.core.mail import send_mail

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
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        
        #send an email
        
        send_mail(
            
           'message from ' + name, #Subject
            message, # message
            email, # from email
           ['temitopeayobami995@gmail.com'], # to email
        )
        return render(request, 'apps/contact.html', {'name':name})
    
    else:
        return render(request, 'apps/contact.html', {})
    
    
def shop(request):
    return render(request, 'apps/shop.html', {})

def checkout(request):
    return render(request, 'apps/checkout.html', {})

def single_product(request):
    return render(request, 'apps/single_product.html', {})

def cart(request):
    return render(request, 'apps/cart.html', {})
        
    
    




