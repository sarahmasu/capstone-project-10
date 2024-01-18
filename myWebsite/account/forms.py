from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserRegistrationForm(UserCreationForm):
  """The class creates a custom user registration form. The form adds first name, passwords, 
     and email fields. The information, entered into the fields will be saved under the User model.

     :param EmailField email: Adds the email field to the form, the help text that appears to help
                              the user user, it is required to enter a username
  """

  email = forms.EmailField(help_text='Enter a valid email address.', required=True)

  class Meta:
      """The class generates the addition fields (first name, username, password1, and password2)
         the get_user_model returns the currently active user model by either a custom model 
         specified in AUTH_USER_MODEL or use the default built-in User
         
         :param AbstractBaseUser model: Returns the user model that is active in this project
         :param list[str] fields: List of fields that will be created
         """
      
      model = get_user_model()
      fields = ['first_name', 'username', 'password1', 'password2']

  def save(self, commit = True):
      """Saves the user's input and adds them to the database under the User model. Returns the
         input to user.

         :param bool commit: Commits the data to the User model
         :param user: The user's input from the UserRegistrationForm is then saved
         :return: user input is saved to User model
         :rtype: Any
      """

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