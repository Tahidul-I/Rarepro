from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from ..product.models import*
from ..cart.models import*
from django.template.loader import render_to_string
import json
import random


def add_to_cart(request):

    # Filtering out the product from ProductVariation Model by the received JSON data through AJAX from add_to_cart.js file

    product_id = request.GET['product_id']
    size = request.GET['dimension']#Vaiable to be renamed as material_dimension in future
    color = request.GET['material_type']#Vaiable to be renamed as material_type in future
    product_size = Size.objects.get(title=size)
    product_color = Color.objects.get(title=color)
    product_variant = ProductVariation.objects.get(size=product_size,color=product_color,product=int(product_id))

    # Crearing a cart dictionary which will be extended in the session cart_data

    cart = {}
    cart[str(product_variant.id)]={
        'title':f"{product_variant.product.title}" ,
        'price':f"{product_variant.selling_price}",
        'slug':f"{product_variant.product.slug}",
        'quantity': request.GET['product_quantity'],
        'image': request.GET['product_image'],
        'color': request.GET['material_type'],
        'size': request.GET['dimension']
    }
    if request.user.is_anonymous:

        # Checking if the session cart_data  is already exist

        if 'cart_data' in request.session:

            # Updating product quantity in session cart_data if the product already exist

            if str(product_variant.id) in request.session['cart_data']:
                cartdata =  request.session['cart_data']
                cartdata[str(product_variant.id)]['quantity'] = int(cartdata[str(product_variant.id)]['quantity'])+int(request.GET['product_quantity'])
                cartdata.update(cartdata)
                request.session['cart_data']=cartdata
                cart_list = request.session['cart_data']
                context={
                    'cart_list':cart_list
                }

                sidebar_template = render_to_string('ajax/product_details_anonymous_user.html',context)
                sidbar_cart_action_template =  render_to_string('ajax/product_detail_sidebar_cart_actions.html')

                return JsonResponse({'sidebar_template':sidebar_template,'sidbar_cart_action_template':sidbar_cart_action_template,'total_cart_items':len(request.session['cart_data'])})
            
            # Adding new product in session cart_data
                
            else:
                cartdata = request.session['cart_data']
                cartdata.update(cart)
                request.session['cart_data']=cartdata
                cart_list = request.session['cart_data']
                context={
                    'cart_list':cart_list
                }

                sidebar_template = render_to_string('ajax/product_details_anonymous_user.html',context)
                sidbar_cart_action_template =  render_to_string('ajax/product_detail_sidebar_cart_actions.html')

                return JsonResponse({'sidebar_template':sidebar_template,'sidbar_cart_action_template':sidbar_cart_action_template,'total_cart_items':len(request.session['cart_data'])})
            
        # Creating the session cart_data if not creaeted

        else:
            request.session['cart_data'] = cart
            cart_list = request.session['cart_data']
            context={
                'cart_list':cart_list
            }
            sidebar_template = render_to_string('ajax/product_details_anonymous_user.html',context)
            sidbar_cart_action_template =  render_to_string('ajax/product_detail_sidebar_cart_actions.html')
            return JsonResponse({'sidebar_template':sidebar_template,'sidbar_cart_action_template':sidbar_cart_action_template,'total_cart_items':len(request.session['cart_data'])})
    
    if request.user.is_authenticated:
        cart_item = None
        try:
            cart_item = UserCart.objects.get(product_variant=product_variant,user=request.user)
        except:
            cart_item = None

        # Updating product quantity if the product already exist in the UserCart Model
        
        if cart_item is not None:
            cart_item.quantity = cart_item.quantity+int(request.GET['product_quantity'])
            cart_item.save()

        # Adding new product to cart if the product not in the UserCart Model

        else:
            user_cart = UserCart(
            user = request.user,
            product_variant = product_variant,
            size = product_variant.size.title,
            title = product_variant.product.title,
            color = product_variant.color.title,
            price = product_variant.selling_price,
            quantity = int(request.GET['product_quantity'])
            )
            user_cart.save()
        
        user_cart = UserCart.objects.filter(user=request.user)
        context={
            'user_cart':user_cart
        }

        sidebar_template= render_to_string('ajax/product_details_authenticated_user.html',context)
        sidbar_cart_action_template =  render_to_string('ajax/product_detail_sidebar_cart_actions.html')
        return JsonResponse({'sidebar_template':sidebar_template,'sidbar_cart_action_template':sidbar_cart_action_template,'total_cart_items':UserCart.objects.filter(user=request.user).count()})



def cart_view(request):
    if request.user.is_anonymous:
        cart_length = 0
        try:
            cart_length = len(request.session['cart_data'])
        
        except:
            cart_length = 0

        if cart_length>=1:
            total_amount = 0
            for product_variant_id,item in request.session['cart_data'].items():
                total_amount+= int(item['quantity'])*float(item['price'])

            cart_list = request.session['cart_data']
            
            context = {
                'cart_list':cart_list,
                'total_amount':int(total_amount),
            }
            return render(request,'cart_view.html',context)
        else:

            return render(request,'empty_cart.html')

    if request.user.is_authenticated:
        cart_length = 0
        try:
           cart_length = UserCart.objects.filter(user=request.user).count()
        
        except:
            cart_length = 0
        
        total_amount = 0

        if cart_length>=1:
            user_cart =  UserCart.objects.filter(user=request.user)
            for cart_item in user_cart:
                total_amount+=cart_item.price*cart_item.quantity

            user_cart = UserCart.objects.filter(user=request.user)
            context = {
                'total_amount':int(total_amount),
                'user_cart':user_cart
            
            }
            return render(request,'cart_view.html',context)
        else:
            return render(request,'empty_cart.html')


def clear_cart(request):
    
    if request.user.is_anonymous:
        try:
            del request.session['cart_data']
        except:
            pass
        
        return render(request,'empty_cart.html')
    if request.user.is_authenticated:
        try:
            query_set = UserCart.objects.filter(user=request.user)
            query_set.delete()
        except:
            pass


    return render(request,'empty_cart.html')

def delete_cart_single_item(request):
    
    product_variant_id = request.GET['product_variant_id']
    if request.user.is_anonymous:
        cart_list = request.session['cart_data']
        del cart_list[product_variant_id]
        request.session['cart_data']=cart_list
        cart_length = len(request.session['cart_data'])
        category = Category.objects.all()
        total_amount = 0
        for product_variant_id,item in request.session['cart_data'].items():
            total_amount+= int(item['quantity'])*float(item['price'])

        
        session_cart = request.session['cart_data']
        print(session_cart)
        context = {
            'session_cart':session_cart
        }

        template = render_to_string('ajax/delete_item_anonymous_user.html',context)
        
    
  
        return JsonResponse({'data':template, 'total_amount':int(total_amount),'total_cart_items':len( request.session['cart_data'])})

    if request.user.is_authenticated:
        selected_cart_item = UserCart.objects.get(user=request.user,product_variant_id=product_variant_id)
        selected_cart_item.delete()
        cart_length = UserCart.objects.filter(user=request.user).count()
        category = Category.objects.all()
        user_cart =  UserCart.objects.filter(user=request.user)
        total_amount = 0
        for cart_item in user_cart:
            total_amount+= cart_item.price*cart_item.quantity

        user_cart =UserCart.objects.filter(user=request.user)
        context={
            'user_cart':user_cart
        }
        template = render_to_string('ajax/delete_item_authenticated_user.html',context)
       

        return JsonResponse({'data':template,'total_amount':int(total_amount),'total_cart_items':UserCart.objects.filter(user=request.user).count()})


def update_cart(request):

    #Receiving JSON data
    json_data = json.loads(request.body.decode('utf-8'))
    #List Unpacking
    changed_product_quantity = json_data.get('updated_cart_quantity_list', []) 

    if request.user.is_anonymous:
        cartdata = request.session['cart_data']
    #  Updating product quantity
        for product_varint_id in changed_product_quantity:
            cartdata[f"{product_varint_id['id']}"]['quantity'] = product_varint_id['quantity']
        
        request.session['cart_data'] = cartdata

        #Calculating total amount of updated cart
        total_amount = 0
        for product_variant_id,item in request.session['cart_data'].items():
            total_amount+= int(item['quantity'])*float(item['price'])
        
        context={
            'cart_list': request.session['cart_data']

        }
        
        template = render_to_string('ajax/updated_cart_anonymous_user.html',context)



        return JsonResponse({'data':template, 'total_amount':total_amount})
    
    if request.user.is_authenticated:
        
        #  Updating product quantity
        for product_varint_id in changed_product_quantity:
            cart_item = UserCart.objects.get(user=request.user,product_variant_id=product_varint_id['id'])
            cart_item.quantity = product_varint_id['quantity']
            cart_item.save()
    
        #Calculating total amount of updated cart
        user_cart =  UserCart.objects.filter(user=request.user)
        total_amount = 0
        for cart_item in user_cart:
            total_amount+= cart_item.price*cart_item.quantity

        context={
            'user_cart':user_cart
        }

        template = render_to_string('ajax/updated_cart_authenticated_user.html',context)

        return JsonResponse({'data':template, 'total_amount':total_amount})