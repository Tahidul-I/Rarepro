from ..category.models import *
from ..site_settings.models import *
from ..cart.models import *
from ..order.models import *
from ..brand.models import *
from django.contrib.auth.models import User
def get_category_and_site_settings(request):
   cart_length = 0
   category = Category.objects.all()
   brands = Brand.objects.all()
   site_data = site_settings.objects.all().first()
   user_cart = None
   user_order_details = None
   if request.user.is_authenticated:
        try:
            cart_length = UserCart.objects.filter(user=request.user).count()
            user_order_details = Order.objects.filter(user = request.user)
        except:
            cart_length = 0
            user_order_details = None

        user_cart = UserCart.objects.filter(user=request.user)[0:2]

   if request.user.is_anonymous:
        try:
            cart_length = len(request.session['cart_data'])
        except:
            cart_length = 0
        

   context = {
        'category':category,
        'site_data':site_data,
        'cart_length':cart_length,
        'user_cart':user_cart,
        'brands':brands,
        'user_order_details':user_order_details
   }

   return context