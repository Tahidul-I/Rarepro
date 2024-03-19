from django.urls import path
from . import views

urlpatterns = [
    path('payment_gateway/',views.payment_gateway,name="payment_gateway"),
    path('payment_complete/',views.payment_complete,name="payment_complete"),
]
