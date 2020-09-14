from django.contrib import admin
from django.utils.html import format_html

from .models import Venue


class VenueAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img width="250px" src="{}" />'.format(obj.image.url)
            )
        return ""

    image_tag.short_description = "Image"
    list_display = ("name", "image_tag", "description", "is_public")


admin.site.register(Venue, VenueAdmin)
