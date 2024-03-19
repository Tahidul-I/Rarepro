from django.shortcuts import render
from ..product.models import *
from ..category.models import *
# Create your views here.
def search_product(request):
    if request.method=="GET":
        searched_words = request.GET.get('search')
        selected_category = request.GET.get('category')

        if selected_category=="All Categories":
            related_products = Product.objects.filter(search_tag__icontains = searched_words)
            context = {
                'related_products':related_products
            }

            return render(request,'search_page.html',context)
        
        else:
            related_products = Product.objects.filter(search_tag__icontains = searched_words,sub_sub_category__sub_category__category__title = selected_category )
            context = {
            'related_products':related_products
            }
                
            return render(request,'search_page.html',context)

