from django.db import models

# Create your models here.

class ShippingCost(models.Model):
    cost = models.FloatField(verbose_name="shipping Cost")

    class Meta:
        verbose_name_plural = "Shipping Cost"

    def __str__(self):
        return f"Shipping Cost - {self.cost}"