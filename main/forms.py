from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class NewUserForm(UserCreationForm):
  email = forms.EmailField(required=True)
  
  class Meta:
    model = User
    fields = [
      'username',
      'email',
      'password1',
      'password2'
    ]




