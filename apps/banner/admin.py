from django.contrib import admin
from .models import*
# Register your models here.
class BannerAdmin(admin.ModelAdmin):
	list_display=['image_tag']

admin.site.register(Banner,BannerAdmin)

