from  django.urls import path
from . import views
urlpatterns = [
    path('search_product/',views.search_product,name="search_product"),
]