from django import forms
from news.models import CustomUser,LANGUAGE_CHOICE, Search

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    email = forms.EmailField(label='E-mail',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    language = forms.ChoiceField(choices = LANGUAGE_CHOICE) 

    class Meta:
        model = CustomUser
        fields = ('username','email','password1','password2','language')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class SearchForm(forms.ModelForm):
    search_request = forms.CharField(label='Search',widget=forms.TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    class Meta:
        model = Search
        fields = ('search_request',)