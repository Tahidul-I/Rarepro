from django.contrib import admin
from .models import *
# Register your models here.

class ProductVariationAdmin(admin.StackedInline):
    model = ProductVariation

class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariationAdmin,ProductImagesAdmin]




admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductVariation)
admin.site.register(ProductImages)
