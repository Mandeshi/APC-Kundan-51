from django import forms
import re

class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Username', 'class': 'form-control'})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'})
    )
    mobile = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter 10-digit Indian Mobile', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        pattern = r'^[a-zA-Z][a-zA-Z0-9_]{4,19}$'
        if not re.match(pattern, username):
            raise forms.ValidationError(
                "Username must start with a letter, be 5-20 characters long, and contain only letters, numbers, or underscores."
            )
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise forms.ValidationError("Invalid email address format.")
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        pattern = r'^[6-9]\d{9}$'
        if not re.match(pattern, mobile):
            raise forms.ValidationError("Mobile number must be a valid 10-digit Indian number starting with 6-9.")
        return mobile

    def clean_password(self):
        password = self.cleaned_data.get('password')
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not re.match(pattern, password):
            raise forms.ValidationError(
                "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character (@$!%*?&)."
            )
        return password
