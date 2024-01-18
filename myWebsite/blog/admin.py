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
    """Displays the title, slug, and status of the post in a list on the Admin site.
       The post can be filtered by their status and can be searched for by their title
       or content.

        :param tuple list_display: A tuple that displays the title, slug, and status of 
                                  the post
        :param tuple list_filter: Tuple filters the post by status
        :param tuple search_fields: Tuple used to search fields by title and content
       """
    
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