from django.forms import ModelForm, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import *

from project_tc_gen.models import Company
from users.models import Profile 
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        widgets = {
            'password': PasswordInput(attrs={
                'type': 'password',
                'style': "width: 50%; height: 50%; font-family: 'Open Sans';font-style: normal;font-weight: 400;font-size: 20px;line-height: 27px;letter-spacing: 0.02em;color: #121212;flex: none;order: 0;flex-grow: 0;",
                'placeholder': "Enter a Password",
        }),
        }
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

# class GenerateDocument(ModelForm):
#     class Meta:
#         model = Document
#         fields = ['document_type']

