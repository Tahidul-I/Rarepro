from django.db import models
from django.utils.html import mark_safe
# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to="uploads/banner_image",verbose_name="Banner Image")
    is_active = models.BooleanField(default=False, verbose_name="Click Checkbox To Activate")

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))





