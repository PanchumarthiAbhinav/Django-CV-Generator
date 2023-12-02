from django import forms
from .models import Client
from .models import User
from .models import CustomUser

# class SignUpForm(forms.Form):
#     name = forms.CharField(max_length=100, required=True)
#     email = forms.EmailField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput, required=True, min_length=8)


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Use PasswordInput widget for password field
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password']


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['y_name', 'position', 'profile', 'location', 'email', 'phone_number', 'linkedin', 'experience', 'education', 'languages', 'skills', 'certificate', 'extracurricular_activities']
        labels = {"y_name":"Name", "profile":"Objective"}
        widgets = {
            'profile': forms.Textarea(attrs={'rows': 3}),  # Set the number of rows for the Textarea widget
            'experience': forms.Textarea(attrs={'rows': 3}),
            'education': forms.Textarea(attrs={'rows': 3}),
            'languages': forms.Textarea(attrs={'rows': 3}),
            'skills': forms.Textarea(attrs={'rows': 3}),
            'certificate': forms.Textarea(attrs={'rows': 3}),
            'extracurricular_activities': forms.Textarea(attrs={'rows': 3}),
        }
