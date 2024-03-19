from django.urls import path
from . import views

urlpatterns = [
    path('user_profile/',views.user_profile,name="user_profile"),
    path('order_view<slug:slug>',views.order_view,name="order_view"),
]
