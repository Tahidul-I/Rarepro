from django.db import models

# Create your models here.
class CouponDiscount(models.Model):
    coupon_code = models.CharField(max_length=60,verbose_name="Cupon Code")
    discount_percentage = models.FloatField(verbose_name="Discount Percentage")

    class Meta:
        verbose_name_plural = "Coupon Discount"
    
    def __str__(self):
        return self.coupon_code