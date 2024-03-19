from django.urls import path
from . import views

urlpatterns = [
    path('product_details/<slug:slug>',views.product_details,name='product_details'),
    path('product_filter/',views.product_filter,name='product_filter'),
    path('filtered_product_paginator/',views.filtered_product_paginator,name='filtered_product_paginator'),
    
]