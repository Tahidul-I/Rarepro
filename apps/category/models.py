from django.db import models
from django.utils.text import slugify 

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "uploads/category_image")
    is_featured = models.BooleanField(default=False)
    banner = models.ImageField(upload_to = "uploads/category_banner",verbose_name="Upload Category Banner")
    slug = models.SlugField(unique=True,blank=True,null=True,help_text="No need to fill out this field")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Category"
    
    def __str__(self):
        return self.title
    


class SubCategory(models.Model):
    category  = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True,null=True,help_text="No need to fill out this field")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SubCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Sub Category"

    def __str__(self):
        return f"{self.category.title}>{self.title}"



class SubSubCategory(models.Model):
    sub_category  = models.ForeignKey(SubCategory, on_delete=models.CASCADE,related_name='sub_sub_category')
    title = models.CharField( max_length=200)
    slug = models.SlugField(blank=True,null=True,help_text="No need to fill out this field")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SubSubCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Sub Sub Category"

    def __str__(self):
        return f"{self.sub_category.category.title}>{self.sub_category.title}>{self.title}"
