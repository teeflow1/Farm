from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('index', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    #path('service/', views.service, name = 'service'),
    #path('product/', views.product, name = 'product'),
    path('contact/', views.contact, name = 'contact_us'),
]