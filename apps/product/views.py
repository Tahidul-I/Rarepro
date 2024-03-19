from django.shortcuts import render,redirect
from django.urls import reverse
from ..product.models import*
from ..brand.models import*
from ..category.models import*
from django.template.loader import render_to_string
from django.http import JsonResponse
import json

def product_details(request,slug):
    product = Product.objects.get(slug=slug)
    product_subsubcategory = product.sub_sub_category
    product_subcategory = product_subsubcategory.sub_category
    product_category = product_subcategory.category

    related_products = Product.objects.filter(
        sub_sub_category__sub_category__category=product_category
    ).exclude(id=product.id)

    product_images = ProductImages.objects.filter(product=product)
    colors = ProductVariation.objects.filter(product=product).values('color__id','color__title').distinct()
    sizes  = ProductVariation.objects.filter(product=product)
    vendor = Brand.objects.get(title=product.brand.title)

    context ={
        'product':product,
        'colors':colors,
        'sizes':sizes,
        'product_images':product_images,
        'vendor':vendor,
        'related_products':related_products,
        
    }

    return render(request,'product_details.html',context)

def product_filter(request):
 
    json_data = json.loads(request.body.decode('utf-8'))
    filtered_object = json_data.get('filter_object', {})
    selected_category = json_data.get('category')
    products_per_page = int(json_data.get('num_of_products'))
    maximum_price =None
    minimum_price = None
    product_category = Category.objects.get(title = selected_category)
    
    brand = None

    try:
        maximum_price = max(filtered_object['max'])
        minimum_price = min(filtered_object['min'])
        price_list = filtered_object['max']
        if not price_list[0]:
            maximum_price
    except:
        maximum_price
    
    try:
        brand = filtered_object['brand']
       
        if not brand[0]:
            brand = None
    except:
        brand = None

    
    if maximum_price is None and brand is None:
        
        return JsonResponse({'redirect_url': reverse('category_filter', args=[product_category.slug])})


    elif brand is None and maximum_price is not None:
    
        all_products =  Product.objects.filter(price__gte=minimum_price,price__lte=maximum_price,sub_sub_category__sub_category__category__title = selected_category)
        total_divided_sections = all_products.count()%products_per_page
  
        if total_divided_sections !=0 :
            number_of_pages = int(1+all_products.count()/products_per_page)
        else:
            number_of_pages = int(all_products.count()/products_per_page)

        
        page_list = list(range(1, number_of_pages+1))

        context = {
            'all_products':all_products[0:products_per_page],
            'product_category':product_category,
            'page_list':page_list,
            'number_of_pages':number_of_pages
        }
        product_template = render_to_string('ajax/filtered_product.html',context)
        pagination_template = render_to_string('ajax/pagination.html',context)

        return JsonResponse({'product_template':product_template,'pagination':pagination_template})

    elif maximum_price is None and brand is not None:
        
        all_products = Product.objects.filter(brand__id__in = brand,sub_sub_category__sub_category__category__title = selected_category)

        total_divided_sections = all_products.count()%products_per_page
     
        if total_divided_sections !=0 :
            number_of_pages = int(1+all_products.count()/products_per_page)
        else:
            number_of_pages = int(all_products.count()/products_per_page)

        # End of number of pages
        
        page_list = list(range(1, number_of_pages+1))

        context = {
            'all_products':all_products[0:products_per_page],
            'product_category':product_category,
            'page_list':page_list,
            'number_of_pages':number_of_pages
        }
        product_template = render_to_string('ajax/filtered_product.html',context)
        pagination_template = render_to_string('ajax/pagination.html',context)

        return JsonResponse({'product_template':product_template,'pagination':pagination_template})


    else:
        
        all_products =  Product.objects.filter(price__gte=minimum_price,price__lte=maximum_price,brand__id__in = brand,sub_sub_category__sub_category__category__title = selected_category)
        
        total_divided_sections = all_products.count()%products_per_page

        if total_divided_sections !=0 :
            number_of_pages = int(1+all_products.count()/products_per_page)
        else:
            number_of_pages = int(all_products.count()/products_per_page)

        # End of number of pages
        
        page_list = list(range(1, number_of_pages+1))

        context = {
            'all_products':all_products[0:products_per_page],
            'product_category':product_category,
            'page_list':page_list,
            'number_of_pages':number_of_pages
        }

       

        product_template = render_to_string('ajax/filtered_product.html',context)
        pagination_template = render_to_string('ajax/pagination.html',context)

        return JsonResponse({'product_template':product_template,'pagination':pagination_template})


def filtered_product_paginator(request):

    json_data = json.loads(request.body.decode('utf-8'))
    filtered_object = json_data.get('checked_items', {})
    max_price = None
    min_price = None
    brand = None
    page_number = json_data.get('page_number')
    products_per_page = json_data.get('products_per_page')
    selected_category = json_data.get('category')
    product_category = Category.objects.get(title = selected_category)
    
    try:
        max_price = max(filtered_object['max'])
        min_price = min(filtered_object['min'])
        price_list = filtered_object['max']
        print( price_list)
        if not price_list[0]:
            max_price = None
    except:
        max_price = None

    try:
        brand = filtered_object['brand']
        print(brand[0])

        if not brand[0]:
            brand = None

    except:
        brand = None

    if max_price is not None and brand is None:
        start_index = (int(products_per_page)*int(page_number))-int(products_per_page)
        end_index = int(products_per_page)*int(page_number)
        all_products =  Product.objects.filter(price__gte=min_price,price__lte=max_price,sub_sub_category__sub_category__category__title = selected_category)[start_index:end_index]
        context = {
            'all_products':all_products,
            'product_category':product_category,
            'page_number':page_number
        }

        product_template = render_to_string('ajax/filtered_product.html',context)
        return JsonResponse({'product_template':product_template})

    elif brand is not None and max_price is None:
        start_index = (int(products_per_page)*int(page_number))-int(products_per_page)
        end_index = int(products_per_page)*int(page_number)

        all_products = Product.objects.filter(brand__id__in = brand,sub_sub_category__sub_category__category__title = selected_category)[start_index:end_index]

        context = {
            'all_products':all_products,
            'product_category':product_category,
            'page_number':page_number
        }

        product_template = render_to_string('ajax/filtered_product.html',context)
        return JsonResponse({'product_template':product_template})

    else:
        start_index = (int(products_per_page)*int(page_number))-int(products_per_page)
        end_index = int(products_per_page)*int(page_number)
        all_products =  Product.objects.filter(price__gte=min_price,price__lte=max_price,brand__id__in = brand,sub_sub_category__sub_category__category__title = selected_category)[start_index:end_index]

        context = {
            'all_products':all_products,
            'product_category':product_category,
            'page_number':page_number
        }

        product_template = render_to_string('ajax/filtered_product.html',context)
        return JsonResponse({'product_template':product_template})
        

    

 