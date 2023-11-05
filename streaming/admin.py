from django.contrib import admin
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from .models import Channel

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'display_image', 'video_url')
    prepopulated_fields = {'slug': ('name',)}  # Auto-populate slug based on name

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" width="50" height="50" />')

    display_image.short_description = 'Image Preview'  # Column header for the image preview

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)
