from django.db import models
from ..category.models import SubSubCategory
from ..brand.models import Brand
from django.utils.text import slugify 
from ckeditor.fields import RichTextField



class Color(models.Model):
    title = models.CharField(max_length=50,unique=True)

    class Meta:
        verbose_name_plural = "Material"

    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=50,unique=True)

    class Meta:
        verbose_name_plural = "Dimension"
   

    def __str__(self):
        return self.title

class Product(models.Model):
    sub_sub_category = models.ForeignKey(SubSubCategory,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="uploads/product_image",verbose_name="Product Thumbnail")
    price = models.FloatField()
    code = models.CharField(max_length=50,verbose_name="SKU")
    short_description = models.TextField()
    description = RichTextField()
    is_featured = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name ="product_vendor")
    tag = models.CharField(max_length=100,verbose_name="Product Tag")
    search_tag = models.CharField(max_length=600,blank=True,null=True,verbose_name="Sensetive",help_text="Do not fill or change this filed")
    slug = models.SlugField(unique=True, blank=True,null=True,max_length=500,help_text="No need to fill out this field")

    def save(self, *args, **kwargs):
        self.search_tag = f"{self.sub_sub_category.sub_category.category.title} {self.sub_sub_category.sub_category.title} {self.sub_sub_category.sub_category.title} {self.sub_sub_category.title} {self.title} {self.tag} "
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs) 
    
    class Meta:
        verbose_name_plural = "Product"
    
    def __str__(self):
        return f"{self.sub_sub_category.sub_category.category.title}>{self.sub_sub_category.sub_category.title}>{self.sub_sub_category.sub_category.title}>{self.sub_sub_category.title}>{self.title}>tag:{self.tag}"
    

       

class ProductVariation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product')
    color = models.ForeignKey(Color,on_delete=models.CASCADE, related_name='color')
    size = models.ForeignKey(Size,on_delete=models.CASCADE, related_name='variant_size')
    selling_price = models.FloatField()
    slug = models.SlugField(unique=True, blank=True,null=True,max_length=500,help_text="No need to fill out this field")

    class Meta:
        verbose_name_plural = "Product Variants"


    def __str__(self):
        return f"Product:{self.product.title}| Color:{self.color.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.product.title}"+ " "+f"{self.color.title}"+f"{self.size.title}")
        super(ProductVariation, self).save(*args, **kwargs) 


class ProductImages(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='related_product')
    image = models.ImageField(upload_to = 'uploads\product_variant_images')

    class Meta:
        verbose_name_plural = "Product Images"

    def __str__(self):
        return f"Porduct:{self.product.title}"
    
    