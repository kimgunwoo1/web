from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import MyMemmer

class MyMemberForm(UserCreationForm) :
    class Meta:
        model = User   #admin User
        fields = ('username','password1','password2','email','first_name','last_name')


