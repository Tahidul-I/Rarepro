from django.shortcuts import render,redirect,reverse
from sslcommerz_lib import SSLCOMMERZ 
from django.views.decorators.csrf import csrf_exempt
from ..order.models import *
from ..cart.models import *
from ..shipping_cost.models import *

def payment_gateway(request):
    
    settings = { 'store_id': 'kuber65d9c2a23469f', 'store_pass': 'kuber65d9c2a23469f@ssl', 'issandbox': True }
    sslcz = SSLCOMMERZ(settings)
    order = Order.objects.get(user=request.user,payment_status = False)
    # order = Order.objects.get(user=request.user,tracking_no = track_no)

    # try:
    #     Order.objects.filter(user=request.user,payment_status = False).delete()
    # except:
    #     pass
    
    # order.save()

    status_url = request.build_absolute_uri(reverse("payment_complete"))
    post_body = {}
    post_body['total_amount'] = order.total
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "12345"
    post_body['success_url'] = status_url
    post_body['fail_url'] = status_url
    post_body['cancel_url'] = status_url
    post_body['emi_option'] = 0
    post_body['cus_name'] = f"{order.first_name} {order.last_name}"
    post_body['cus_email'] = order.email
    post_body['cus_phone'] = order.phone
    post_body['ship_name' ] = "Madbangla"
    post_body['ship_add1' ] = order.address
    post_body['ship_city' ] = order.division
    post_body['ship_country' ] = order.country
    post_body['ship_postcode' ] = order.post_code
    post_body['cus_add1'] = order.address
    post_body['cus_city'] = order.division
    post_body['cus_country'] = order.country
    post_body['shipping_method'] = "YES"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Mixed"
    post_body['product_profile'] = "general"

    response = sslcz.createSession(post_body) #API Response

    return redirect(response['GatewayPageURL'])

@csrf_exempt
def payment_complete(request):
    if request.method=='POST' or request.method=='post':
        payment_data = request.POST
        status = payment_data['status']

        if status =="VALID":
            payment_status = "VALID"
            return redirect('order_page',payment_status)

        else:

            payment_status = "FAILED"
            return redirect('order_page',payment_status)