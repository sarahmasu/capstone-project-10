from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# Explanation of Mehtod
# __________________________
'''
    The @login_required function, prevents the user from
    accessing the page, once they have logged in or signed up
    they will be redirected to the home page but they will now 
    have access to the library page.
'''

@login_required(login_url='login')
def view_library(request):
    return render(request,'library.html')

# Reference:
# _________________________
'''
    - Wanted to force users into logging in or signing up before
      they can access the Library page.
      Sources: https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-login-required-decorator
               https://studygyaan.com/django/how-to-restrict-access-with-django-login-required-decorator-function
               https://stackoverflow.com/questions/69099712/how-to-restrict-pages-in-django-if-login-requiredlogin-url-login-does-no
'''
