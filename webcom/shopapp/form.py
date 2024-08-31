from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomerUserForm(UserCreationForm):
    username  = forms.CharField(widget=forms.TextInput(attrs={'class' :'form-control','placeholder':'Enter User Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class' :'form-control','placeholder':'Enter Email Name'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' :'form-control','placeholder':'Enter Your  Password '}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' :'form-control','placeholder':'Confirm  Your Pasword'}))

    
    class Meta:
        model =User
        fields = ['username','email','password1','password2']