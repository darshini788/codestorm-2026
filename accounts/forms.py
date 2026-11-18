from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class StudentRegistrationForm(forms.ModelForm):
    usn = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '4RA24CS028'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91 9876543210'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Enter address'}))
    department = forms.ChoiceField(choices=UserProfile.DEPT_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    semester = forms.ChoiceField(choices=UserProfile.SEM_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    avatar = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Choose password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'student@rit.edu'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        }

class UserProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    usn = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    department = forms.ChoiceField(choices=UserProfile.DEPT_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    semester = forms.ChoiceField(choices=UserProfile.SEM_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    avatar = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ['usn', 'phone_number', 'address', 'department', 'semester', 'avatar']
