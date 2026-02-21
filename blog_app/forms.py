from django import forms
from django.contrib.auth.forms import UserCreationForm

from blog_app import models
from blog_app.models import Login, Users, Blog


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Login

        fields = ('username', 'password1', 'password2')


class UsersRegister(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('name', 'email','bio','document')

class BlogRegister(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','content','document','date')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

        }