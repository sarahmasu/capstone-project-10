from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    # Returns all posts that are with status 1 (published) abd order from the latest one.

    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
