from django.db import models

# Create your models here.
class site_settings(models.Model):
    logo = models.ImageField(upload_to = 'uploads\site_logo',verbose_name="Upload Site Logo")
    welcome_message = models.CharField(max_length=600, verbose_name="Write Welcome Message")
    facebook_link = models.CharField(max_length=600,verbose_name="Facebook Page Link")
    instagram_link = models.CharField(max_length=600,verbose_name="Instagram Link")
    twitter_link = models.CharField(max_length=600,verbose_name="Twitter Link")
    fav_icon = models.ImageField(upload_to = 'uploads\Favicon',verbose_name="Upload Fav Icon")
    phone = models.CharField(max_length=11, verbose_name="Phone")
    email = models.EmailField()
    image = models.ImageField(upload_to="uploads/product_detail_advertisement_image",verbose_name="Upload Image (For advertisement on product detail page)")

    class Meta:
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return f"Site settings info"
    