from django.shortcuts import render,redirect,HttpResponse
from ..category.models import *
from ..product.models import *
from ..brand.models import *
from django.core.paginator import Paginator

def category_filter(request,slug):
    
    product_category = Category.objects.get(slug=slug)
    products =  Product.objects.filter(sub_sub_category__sub_category__category = product_category)
    products_per_page = 2
    total_divided_sections = products.count()%products_per_page
    brands = Brand.objects.all()
    
    if total_divided_sections !=0 :
        number_of_pages = int(1+products.count()/products_per_page)
    else:
        number_of_pages = int(products.count()/products_per_page)

    page_list = list(range(1, number_of_pages+1))

    #Pagination functionality

    paginator = Paginator(products, products_per_page)  
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)


    try:
        page_number = int(page_number)
    except:
        pass

    context = {
        'product_category':product_category,
        'products':products,
        'brands':brands,
        'page_number':page_number,
        'page_list':page_list,
        'number_of_pages':number_of_pages,
        'products_per_page':products_per_page
    
    }
    return render(request,"category_filter.html",context)
    
   
def sub_sub_category_filter(request,slug):
    subsub_category = SubSubCategory.objects.get(slug=slug)
    products = Product.objects.filter(sub_sub_category = subsub_category)
    
    context = {
        'products':products,
        'subsub_category':subsub_category,
    }
    return render(request,'sub_sub_category_filter.html',context)
