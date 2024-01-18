from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# The status of the post, if the post is still in draft or has been published
STATUS = ((0, "Draft"), (1, "Publish"))

# This class creates a table called Post
class Post(models.Model):
    """Creates a table called Post in database. The input captured will be saved in the database. 
       The post is sorted from newest to the oldest post. The title will be displayed on the Post
       table.
       
        :param AutoField id: auto generates ids for post objects
        :param CharField title: creates a charfield, max length is 300, and each title must be unique
        :param CharField slug: creates a charfield, max length is 300, and each title must be unique
        :param ForeignKey[User] author: retrieves the username from the User table, the post get deleted
                                        when the user is deleted
        :param TextField content: creates a charfield allowing the user to add content to the post
        :param IntegerField status: creates a dropdown where the user selects the status of the post,
                                    either 0 - draft or 1 - published
        :param DateTimeField created_at: datetimefield will be used to get the date the post was created, 
                                         the dates can either use the current date or another date
        :param DateTimeField updated_at: datetimefield will be used to get the date the post was created, 
                                         the dates can either use the current date or another date
       """
    # Unique id given to each post.
    id = models.AutoField(primary_key=True)

    # Title of the post.
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)

    # The author of the post, this will be the user who created the post.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # The content of the post.
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    # The date the post was created will use the current date
    # The update date will use the current date.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # This class orders the post created from the newest to oldest.
    class Meta:
        """Sorts the post object from the newest to the oldest posts.
        
            :param list ordering: a list of ordered post object
        """
        ordering = ["-created_at"]

    # Returns tbe title in a readable form
    def __str__(self):
        """Returns the title in a readable form.

            :return: the title is returned in a readable form
            :rtype: str
        """
        return self.title

"""
    Reference:
    ------------------
        * Wanted to be add more information to the blog.
        Source: https://medium.com/geekculture/create-a-blog-with-django-60f529f1d8b6
                https://sentry.io/answers/slug-in-django/#:~:text=Slug%20is%20a%20term%20from,in%20a%20human%2Dfriendly%20form.
"""
