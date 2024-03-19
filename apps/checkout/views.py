from django.shortcuts import render,redirect,HttpResponse
from ..category.models import*
from ..cart.models import*
from ..site_settings.models import *
from django.contrib.auth.decorators import login_required
from ..shipping_cost.models import *


# @login_required(login_url='user_sign_in')
def checkout(request):
   
    if request.user.is_authenticated:

        user_cart_all_item  = UserCart.objects.filter(user=request.user)
        total_amount = 0
        for cart_item in user_cart_all_item:
            total_amount+= cart_item.price*cart_item.quantity
        
        shipping_cost = ShippingCost.objects.all().last()
        sub_total = total_amount
        total_amount = total_amount +shipping_cost.cost
        
        context={
            'sub_total':sub_total,
            'user_cart_all_item':user_cart_all_item,
            'total_amount':total_amount,
            'shipping_cost':shipping_cost,
        }

        return render(request,'checkout.html',context)
        
    else:
        return redirect('user_sign_in')

