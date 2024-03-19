from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from ..cart.models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash

# Create your views here.

def user_signup(request):

    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_status = True
        try:
            user = User.objects.get(username=username)
            user_status = True
        except:
            user_status = False
        
        if user_status == False:
            if password==confirm_password:
                password_1 = make_password(password)
                user =User.objects.create(first_name=first_name,last_name=last_name,username = username, password = password_1, email =email)
                user.save()
                success_message = 'Registration Successfull!'
                message_type = "success"
              
                return redirect('user_login_page',success_message,message_type)
            else:
                error_message = 'Password fields does not match. Please try again.'
                message_type = "error"
                
                return redirect('user_signup_page',error_message,message_type)
            
            
        else:
            info_message = 'Username Already Exist!'
            message_type = "info"

            return redirect('user_signup_page',info_message,message_type)
           
        
    else:
        
        return render(request,'signup.html')

def user_sign_in(request):

    if request.user.is_authenticated:

        user_cart_items = UserCart.objects.filter(user = request.user)

        if not user_cart_items.exists():
            try:

                for product_variant,item in request.session['cart_data'].items():
                    product_variant_id = product_variant
                    user_cart = UserCart(
                    user = request.user,
                    product_variant_id = product_variant_id,
                    size = item['size'],
                    title = item['title'],
                    color = item['color'],
                    price =float( item['price']),
                    quantity = int( item['quantity'])
                    )

                    user_cart.save()
                
                return redirect('index')
               

            except:
                
                return redirect('index')
        else:
            return redirect('index')
               
               

           


           

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = "anonymous"
        try:
            user = User.objects.get(username=username)
        except:
            user = "anonymous"

        if user !="anonymous":
            if check_password(password,user.password):
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')

                user_cart_items = UserCart.objects.filter(user = request.user)
                # checking if the user has any item in cart. If not, updating the user cart model from session cart_data
                if not user_cart_items.exists():
                   
                    try:
                        for product_variant,item in request.session['cart_data'].items():
                                product_variant_id = product_variant
                                user_cart = UserCart(
                                user = request.user,
                                product_variant_id = product_variant_id,
                                size = item['size'],
                                title = item['title'],
                                color = item['color'],
                                price =float( item['price']),
                                quantity = int( item['quantity'])
                                )

                                user_cart.save()
                    except:
                        pass
                    
                    
                return redirect('index')

            else:
                cart_length = 0
                info_message = "Invalid password"
                message_type = "info"

                return redirect('user_login_page',info_message,message_type)

        else:
            cart_length = 0
            info_message = "Username Does Not Exist"
            message_type = "info"  

            return redirect('user_login_page',info_message,message_type)

    else:
      
        return render(request,'login.html')


def user_logout(request):
    
    logout(request)
    return redirect('user_sign_in')





def user_login_page(request,message,message_type):

    if message_type == "info":

        context = {
                'info_message':message
            }

        return render(request,'login.html',context)

    elif message_type == "success":
        context = {
                'success_message':message
            }

        return render(request,'login.html',context)
   

def user_signup_page(request,message,message_type):
    if message_type == "error":
        context = {
            'error_message':message
        }

        return render(request,'signup.html',context)
    
    elif message_type == "info":
        context={
            'info_message':message

        }

        return render(request,'signup.html',context)