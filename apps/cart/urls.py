from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('cart_view/',views.cart_view,name='cart_view'),
    path('clear_cart/',views.clear_cart,name='clear_cart'),
    path('delete_cart_single_item/',views.delete_cart_single_item,name='delete_cart_single_item'),
    path('update_cart/',views.update_cart,name='update_cart'),
    
]