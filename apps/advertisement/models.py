from django.db import models
from django.utils.html import mark_safe
# Create your models here.

class Adds(models.Model):
    image = models.ImageField(upload_to="uploads/adds_image")

    
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    class Meta:
        verbose_name_plural = "Home Page Advertisement"


    
