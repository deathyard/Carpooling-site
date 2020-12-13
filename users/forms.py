from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm): # Registration form for user
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2'] # Fields along with order to be displayed on page 

class UserUpdateForm(forms.ModelForm): # Form for updating an user 
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm): # Form for updating the profile linked with user
    class Meta:
        model = Profile
        fields = ['image','first_name','last_name','contact_no']