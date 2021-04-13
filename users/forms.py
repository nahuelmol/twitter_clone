from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 

from django import forms

class registerForm(forms.Form):
	username = forms.CharField(label='username',max_length = 20)
	email = forms.CharField(label='emial',max_length=20)
	password = forms.CharField(label='password',max_length=20, widget=forms.PasswordInput)

class loginForm(forms.Form):
	username = forms.CharField(label='username',max_length = 20)
	password = forms.CharField(label='password',max_length=20, widget=forms.PasswordInput)	


