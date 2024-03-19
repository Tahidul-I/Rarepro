from django.urls import path
from . import views

urlpatterns = [
    path('order_complete/',views.order_complete,name="order_complete"),
     path('order_page/<str:payment_status>',views.order_page,name="order_page"),
]
