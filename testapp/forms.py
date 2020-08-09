from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 30)
    email = forms.CharField(max_length = 30)
    password = forms.CharField(widget=forms.PasswordInput())
    passwordconfirm = forms.CharField(widget = forms.PasswordInput(), label="Confirm Password")

    def clean(self):
        password = self.cleaned_data.get('password')
        passwordconfirm = self.cleaned_data.get('passwordconfirm')
        if password != passwordconfirm:
            raise forms.ValidationError('Password must match.')
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # print(email.contains("gmail.com"))
        if not "gmail.com" in email:
            raise forms.ValidationError('Email must be gmail.com')

        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('Email must be unique')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        exists = User.objects.filter(username = username).exists()
        if exists:
            raise forms.ValidationError('Username must be unique')

        return username




