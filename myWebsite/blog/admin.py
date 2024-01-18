from django.contrib import admin
from .models import Post

# Register your models here.

# Explanation of Class
# =====================
"""
    The class will only display the title, slug, and status of the post in a list of posts
    The post can be filtered by the status of the post.
    The post can be searched by using either the title or the content.
"""
# =====================
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "status",
    )
    list_filter = ("status",)
    search_fields = (
        "title",
        "content",
    )

admin.site.register(Post, PostAdmin)