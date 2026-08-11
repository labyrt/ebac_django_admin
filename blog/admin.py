from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Configura a apresentação e a busca de posts no Django Admin."""

    list_display = ("title", "author", "published", "created_at")
    list_filter = ("published", "created_at")
    search_fields = ("title", "body", "author__username")
