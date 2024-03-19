from django.urls import path
from . import views

urlpatterns = [
    path('brand_list/',views.brand_list,name='brand_list'),
    path('brand_store/<slug:slug>',views.brand_store,name='brand_store'),
    
]
