from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class BookModelForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','publisher','language','pages','summary']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'publisher':forms.TextInput(attrs={'class':'form-control'}),
            'language':forms.TextInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'summary':forms.Textarea(attrs={'class':'form-control','rows':3,'col':2}),
        }
        
class SignUpForm(UserCreationForm):
    password2=forms.CharField(label='Conforim Password (agin)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email']
        labels={
            'email':"Email",
        }
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            # 'first_name':forms.TextInput(attrs={'class':'form-control'}),
            # 'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True,'class':'form-control'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'class':'form-control'}),
    )
    class Meta:
        model=User
        fields=['username','password']
        