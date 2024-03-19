from django.db import models
from django.contrib.auth.models import User
from ..product.models import*
# Create your models here.
class UserCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariation,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name='Product Name')
    size = models.CharField(max_length=100,verbose_name='Product Size')
    color = models.CharField(max_length=100,verbose_name='Product Color')
    price = models.FloatField(verbose_name='Product Price')
    quantity = models.IntegerField(verbose_name='Product Quantity')

    class Meta:
        verbose_name_plural = 'Cart'

    def __str__(self):
        return f"{self.title}|{self.size}|{self.color}"
    

