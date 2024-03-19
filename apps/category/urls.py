from django.urls import path
from . import views

urlpatterns = [
    path('category_filter/<slug:slug>',views.category_filter,name='category_filter'),
    path('sub_sub_category_filter/<slug:slug>',views.sub_sub_category_filter,name='sub_sub_category_filter'),
    
]