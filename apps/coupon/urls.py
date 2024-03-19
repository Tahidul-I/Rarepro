from django.urls import path
from . import views

urlpatterns = [
    path('coupon_discount/',views.coupon_discount,name='coupon_discount'),
]
