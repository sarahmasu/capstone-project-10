from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    """Sorts and creates a list of posts from the newest to the oldest post.

        :param BaseManager queryset: Calls the Post class and filters the posts
                                     by status 1 (published) then sort it by date
                                     created from the newest to oldest
        :param Literal template_name: The name of the template the content will be 
                                      rendered on
    """

    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    """Renders the content from the post onto the webpage.
    
        :param Post model: Calls the Post class from the models.py
        :param Literal template_name: The name of the template the content will be 
                                      rendered on
    """

    model = Post
    template_name = 'post_detail.html'

"""
    Reference:
    ------------------
        * Wanted to be add more information to the blog.
        Source: https://medium.com/geekculture/create-a-blog-with-django-60f529f1d8b6
                https://sentry.io/answers/slug-in-django/#:~:text=Slug%20is%20a%20term%20from,in%20a%20human%2Dfriendly%20form.
"""