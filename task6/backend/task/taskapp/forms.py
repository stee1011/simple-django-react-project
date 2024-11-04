from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Correct import for User model
from django.forms import EmailInput

# Creation of form for the Students model
class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Students
        fields = '__all__'

# User Registration Form for authentication
class UserRegistrationForm(UserCreationForm):
    # Email field customization
    email = forms.EmailField(
        required=True,
        max_length=30,
        widget=EmailInput(attrs={
            'placeholder': 'Email Address',
            'class':'email-field',
            'id':'email-id'
            })
    )

    class Meta:
        model = User  # Use the correct User model
        fields = [
            'first_name', 'email', 'password1', 'password2'
        ]

    def clean_email(self):  # Correct naming for the validation method
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise form.ValidationError("it must have etters only")
        return first_name

