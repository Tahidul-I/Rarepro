from django.db import models
from django.utils.text import slugify 
from ckeditor.fields import RichTextField


# Create your models here.

class Brand(models.Model):
    title = models.CharField(max_length=100,verbose_name="Name Of The Brand")
    image = models.ImageField(upload_to="uploads/Vendor_banner",verbose_name="Brand banner")
    logo = models.ImageField(upload_to="uploads/brand_logo",verbose_name="Brand Logo")
    short_description = models.TextField(verbose_name="Short Description About The Brand")
    description = RichTextField(verbose_name="Add an ellaborate description about the Brand")
    phone = models.CharField(max_length=11,verbose_name="Contact Number")
    facebook_link = models.CharField(max_length=600,verbose_name="Facebook Profile Link")
    instagram_link = models.CharField(max_length=600,verbose_name="Instagram Profile Link")
    location = models.CharField(max_length=600,verbose_name="Provide a detailed address of the Brand showroom")
    slug = models.SlugField(unique=True,blank=True,null=True,help_text="No need to fill out this field")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Brand, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Brand Information'


    def __str__(self):
        return self.title
    