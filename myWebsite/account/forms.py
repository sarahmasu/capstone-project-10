from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Explanation of Class:
# _______________________________
'''
    - In this class a user creation form is created with custom register form.
    - Using UserCreationForm, we can add the first name, username, and password to
      the form.
    - The Meta class generates the textboxes and fields for the first name, username, email,
      password.
        - The get_user_model will return the currently active user model by 
          either a custom model specified in AUTH_USER_MODEL or use the default built-in User.
    - The save method saves the input to the database under the User model.

'''
# ________________________________
# End of Explanation

class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField(help_text='Enter a valid email address.', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'username', 'password1', 'password2']

    def save(self, commit = True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user


# References:
# _________________________________
'''
   - Explanation of get_user_model() function
     Source: https://www.geeksforgeeks.org/how-to-use-user-model-in-django/
    
    - Needed help adding the email field to the page.
      Source: https://pylessons.com/user-registration
'''