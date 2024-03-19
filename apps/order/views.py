from django.shortcuts import render,HttpResponse,redirect
from ..cart.models import *
from ..shipping_cost.models import *
from .models import *
import random


def order_complete(request):
    if request.method == 'POST':
        try:
            existing_order = Order.objects.get(user=request.user,payment_status=False)
            existing_order.delete()
        except:
            pass

        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        division = request.POST.get('division')
        address = request.POST.get('street-address')
        post_code = request.POST.get('postcode')
        country = request.POST.get('country')
        payment_mode = request.POST.get('payment_mode')
    
        cart_items = UserCart.objects.filter(user=request.user)
        sub_total = 0

        # Calculating cart total amount

        for item in cart_items:
            sub_total += item.quantity*item.price
        
        shipping_cost = ShippingCost.objects.all().first()
        total_amount = sub_total+shipping_cost.cost

        track_no = str(random.randint(111111,999999))

        # Checking if the track_no already exist and if not, settigs the random number as track number
        
        while Order.objects.filter(tracking_no=track_no) is None:
            track_no = str(random.randint(111111,999999))

        # Saving order details into Order Model
    
        order_data = Order(
            user = request.user,
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone = phone,
            division = division,
            address = address,
            post_code = post_code,
            country = country,
            total = total_amount,
            payment_mode = payment_mode,
            tracking_no = track_no
        )
        order_data.save()

        # Saving ordered products in OrderItem Model

        for item in cart_items:
            OrderItem.objects.create(
                order = order_data,
                product = item.product_variant,
                price = item.price,
                quantity = item.quantity
            )

       
        if payment_mode == "COD":
            order_data.payment_mode = "Cash On Delivery"
            order_data.save()
            payment_mode = "COD"
            return redirect('order_page',payment_mode)

        else:
            order_data.payment_mode = "Online Payment"
            order_data.save()

            return redirect('payment_gateway')

    


def order_page(request,payment_status):
    order_success_status = False
    payment_status_message = payment_status
    if payment_status_message=="VALID" or payment_status_message=="COD":
        order_success_status = True
        order_details =Order.objects.filter(user=request.user).order_by('-created_at').first()
        order_details.payment_status = True
        order_details.save()
        user_cart = UserCart.objects.filter(user=request.user)
        user_cart.delete()
        shipping_cost = ShippingCost.objects.all().first()
        sub_total = 0
        for item in order_details.order_item.all():
            sub_total += item.quantity*item.price

        context = {
            'order_details':order_details,
            'shipping_cost':shipping_cost,
            'sub_total':int(sub_total),
            'order_success_status':order_success_status
        }

        return render(request,'order.html',context)

    elif payment_status_message=="FAILED":
        context = {
            'order_success_status':order_success_status
        }
        return render(request,'order.html',context)



