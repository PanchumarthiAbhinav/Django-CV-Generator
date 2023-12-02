from django import forms
from .models import Client
from .models import User
from .models import CustomUser


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Use PasswordInput widget for password field
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password']


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class ClientForm(forms.ModelForm):
    extracurricular_activities = forms.CharField(label='Extracurricular Activities', widget=forms.Textarea(attrs={'rows': 3}), required=False)

    class Meta:
        model = Client
        fields = ['y_name', 'position', 'profile', 'location', 'email', 'phone_number', 'linkedin', 'experience', 'education', 'languages', 'skills', 'certificate', 'extracurricular_activities']
        labels = {'y_name': 'Name', 'profile': 'Objective'}
        widgets = {
            'profile': forms.Textarea(attrs={'rows': 3}),
            'experience': forms.Textarea(attrs={'rows': 3}),
            'education': forms.Textarea(attrs={'rows': 3}),
            'languages': forms.Textarea(attrs={'rows': 3}),
            'skills': forms.Textarea(attrs={'rows': 3}),
            'certificate': forms.Textarea(attrs={'rows': 3}),
        }