from django.contrib import admin

from news.models import Post

def is_published(obj):
    return not obj.is_draft
is_published.boolean = True
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", is_published, "date_published"]


admin.site.register(Post, PostAdmin)
