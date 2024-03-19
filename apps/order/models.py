from django.db import models
from django.utils.text import slugify 
from django.contrib.auth.models import User
from ..product.models import *
# Create your models here.
class Order(models.Model):
    ORDER_STATUS = [
        ('is currently on pending', 'is currently on pending'),
        ('has been received', 'has been received'),
        ('is being shipped', 'is being shipped'),
        ('has been delivered', 'has been delivered'),
    ]


    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250,verbose_name="First Name")
    last_name = models.CharField(max_length=250,verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=14,verbose_name="Contact Number")
    division = models.CharField(max_length=50,verbose_name="Division")
    address =models.TextField(verbose_name="Address")
    post_code = models.CharField(max_length=50,verbose_name="Post Code")
    country = models.CharField(max_length=100,verbose_name="Country Name")
    total = models.FloatField(verbose_name="Total Payment")
    payment_mode = models.CharField(max_length=250)
    payment_id = models.CharField(max_length=250,null=True,blank=True)
    order_status = models.CharField(max_length=250,default="is currently on pending",choices = ORDER_STATUS,verbose_name="Order Status")
    tracking_no = models.CharField(max_length=250,verbose_name = "Tracking ID")
    created_at = models.DateTimeField(auto_now_add = True,verbose_name="Creating Date")
    updated_at = models.DateTimeField(auto_now = True,verbose_name= "Updating Date")
    payment_status = models.BooleanField(default=False,verbose_name="Placed order?")
    slug = models.SlugField(unique=True,blank=True,null=True)

    class Meta:
        verbose_name_plural = 'Orders'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.division+self.tracking_no)
        super(Order, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.id}-{self.tracking_no}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_item")
    product = models.ForeignKey(ProductVariation,on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order.id}-{self.order.tracking_no}"
    




