from django.shortcuts import render,redirect,HttpResponse
from ..product.models import *
from ..brand.models import *

def brand_list(request):
    vendors = Brand.objects.all()
    nav_brand = "active"
    context={
            'vendors':vendors,
            'nav_brand':nav_brand
    } 
    return render(request,"vendor_list.html",context)
    

def brand_store(request,slug):
    vendor = Brand.objects.get(slug=slug)
    products = Product.objects.filter(brand=vendor)
    featured_products = Product.objects.filter(brand=vendor,is_featured=True)

    if featured_products.exists():
        context={
            'vendor':vendor,
            'products':products,
            'featured_products':featured_products
        }
        
        return render(request,"vendor_store.html",context)
    else:
        context={
            'vendor':vendor,
            'products':products,
        }
        
        return render(request,"vendor_store.html",context)
    