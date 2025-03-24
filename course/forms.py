from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Signup


class StudentForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Signup
        fields = "__all__"

class EditForm(forms.ModelForm):   
    class Meta:
        model = Signup
        fields = ['firstName', 'lastName', 'email']

