from django.contrib import admin
from .models import*
# Register your models here.

class AddAdmin(admin.ModelAdmin):
    list_display=['image_tag']
    def has_add_permission(self, request):
            existing_objects_count = Adds.objects.count()
            return existing_objects_count < 2


admin.site.register(Adds,AddAdmin)