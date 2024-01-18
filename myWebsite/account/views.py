from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

# Explanation of Method:
# _____________________________
"""
    - In the register method the form is generated and allows the user 
      to create an account:
        -  If the user is logged in, they will be prevented from creating
           a user account.
        - If the user is not logged they will be able to create an account.
            - If the request method is POST, all the information the user
              has entered into the textbox will be sent to the database.
                - The form is rendered.
                - The user needs to be valid in order for the information to be
                saved.
                - Once the information is saved, the 
                - The user will be redirected to the login page to be logged in.
                - A message will display that the account has been successfully created
            - If the account fails to be created, an error message will be displayed.
        - Else the call the UserRegistrationForm function
        The method will render the form from the register.html page.
"""
# ______________________________
# End of Explanation


def register(request):
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
