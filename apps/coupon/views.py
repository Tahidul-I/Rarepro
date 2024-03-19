from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
def coupon_discount(request):
    coupon_code = request.GET.get('coupon_code')
    total_cost = float(request.GET.get('total_cost'))
    subtotal_amount = float(request.GET.get('subtotal_amount'))
    
    existing_coupons_and_discounts = CouponDiscount.objects.all()
    total_amount = 0
    discounted_amount = 0
    for coupon in existing_coupons_and_discounts:
        if coupon_code == coupon.coupon_code:
            discount = float(coupon.discount_percentage/100)

            discounted_amount = total_cost*discount
            total_amount = subtotal_amount - discounted_amount
            break;
    
    return JsonResponse({'total_amount':int(total_amount),'discounted_amount':int(discounted_amount)})
