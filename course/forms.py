from django import forms
# from django.contrib.auth.models import User
from .models import Signup,Image


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

class StudentForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Signup.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    class Meta:
        model = Signup
        fields = ['username', 'email', 'firstName', 'lastName', 'password']  # Explicitly include necessary fields


class EditForm(forms.ModelForm):   
    class Meta:
        model = Signup
        fields = ['firstName', 'lastName', 'email']

class ImgForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        

