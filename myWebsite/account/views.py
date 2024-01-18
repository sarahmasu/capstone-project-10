from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def register(request):
    """Generates the registration form by calling the UserRegistrationForm class from forms.py
       If the user is logged in, they will be redirected to the home page. If the user is not logged 
       in and does not have an account they will be redirected to the register webpage to create an 
       account, once they filled in the fields the user will be redirected to the home page. If a problem
       occurs when the user tries to create an account, an error message will be displayed when the 
       registration web page will be reload. The register.html page will be user to render the form.
      
       :param request: Used to procress any HttpResponse requests
       :param user: Used to call the save function from the forms.py to save the user's input
       :param error: Returns the error if an issue arises
       :return: HttpResponse calls the django.template.loader.render_to_string function with parsed arguements
                to render the form on the register.html page
       :rtype: HttpResponse
    """
    
    if request.user.is_authenticated:
        return redirect("/home/")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created for {user.username}")
            return redirect("/home/")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})


# Explanation of Method
# _______________________________
"""
    - The 'custom_logout' logs out the user when they click on the log out
      link in the navbar.
    - The method will also print out a custom message to indicate that the user
      successfully logged out.
    - It redirects the user to another webpage.
"""


@login_required
def custom_logout(request):
    """When the user logs out of their account, a message will display to indicate that
       they have successfully logged out.
       
       :param request: Used to procress any HttpResponse requests
       :return: Redirects the user to the home web page
       :rtype: HttpResponseRedirect
       """
    
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/home/")


# Explanation of Method
# _______________________________
'''
    - The method checks if the user is logged in, if so the user will be
      redirected back to the homepage.
    - If the user is not logged in the user will be redirected to the login page
      to log into their user account.
    - The AuthenticationForm checks if the username and password is in the database.
    - Once authentication is completed the user is redirected to the homepage.
'''

def custom_login(request):
    """Logs the user into the account. The user is required to fill all the field,
       the credentials entered will be checked in the User model. 
       - If they match they user will be redirected to the home webpage and a message 
         will display that they have successfully logged into their account. 
       - If the credentials are invalid, an error 
         message will be displayed for the user to see, the form will be reloaded. 
        - If the 
          user is logged in and try to log in, they will be redirected to the home web page.
       
       :param request: Used to procress any HttpResponse requests
       :param form: Calls the AuthenticationForm class
       :param user: Calls the authenticate function to check the credentials of username and password
       :param error: Returns the error if an issue arises
       :return: HttpResponse calls the django.template.loader.render_to_string function with parsed arguements
                to render the form on the login.html page
       :rtype: HttpResponse
       """
    
    if request.user.is_authenticated:
        return redirect("/home/")
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {user.username}!")
                return redirect("/home/")
        
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


# References:
# _________________________________
"""
    - Wanted to prevent the signed in user from creating an account.
      Source: https://pylessons.com/user-registration

    - Wanted to website to display a message if the account was successfully created.
      Source: https://pylessons.com/django-messaging

    - Struggled with the logout and login function of the website.
      Source: https://pylessons.com/django-login-logout
"""
