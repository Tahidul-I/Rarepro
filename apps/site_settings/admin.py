from django.contrib import admin
from .models import site_settings
# Register your models here.
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
            existing_objects_count = site_settings.objects.count()
            return existing_objects_count < 1


admin.site.register(site_settings,SiteSettingsAdmin)