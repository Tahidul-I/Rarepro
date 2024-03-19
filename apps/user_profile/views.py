from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from ..order.models import *
from ..shipping_cost.models import *
# Create your views here.
def user_profile(request):
    user = User.objects.get(username=request.user.username)
    order_details = Order.objects.filter(user = request.user)
    context = {
        'user':user,
        'order_details':order_details
    }

    return render(request,'my_account.html',context)

def order_view(request,slug):
  
    order = Order.objects.get(slug=slug)
    
    # calculating subtotal
    sub_total = 0

    for item in order.order_item.all():
        sub_total += (item.price*item.quantity)
        
    
    shipping_cost = ShippingCost.objects.all().first()
    context = {
        'order':order,
        'sub_total':sub_total,
        'shipping_cost':shipping_cost
    }

    return render(request,'order_view.html',context)

    