from django.shortcuts import render,redirect,HttpResponse
from ..product.models import*
from ..banner.models import*
from ..advertisement.models import*
from ..brand.models import*
from ..cart.models import *
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    
    if request.user.is_authenticated:

        banner = Banner.objects.filter(is_active=True)
        adds = Adds.objects.all()
        products = Product.objects.filter(is_featured=True)
        brands = Brand.objects.all()
        context = {
            'banner':banner,
            'adds':adds,
            'products':products,
            'brands':brands,
            
        }
        return render(request, 'index.html',context)

    if request.user.is_anonymous:
  
        banner = Banner.objects.all()
        adds = Adds.objects.all()
        products = Product.objects.filter(is_featured=True)
        brands = Brand.objects.all()
        context = {
            'banner':banner,
            'adds':adds,
            'products':products,
            'brands':brands,
        }
        return render(request, 'index.html',context)

def about_us(request):
    nav_about = "active"
    context = {
        'nav_about':nav_about
    }

    return render(request,'about_us.html',context)

def contact_us(request):
    nav_contact = "active"
    context = {
        'nav_contact':nav_contact
    }

    return render(request,'contact_us.html',context)





        
    

        
    

