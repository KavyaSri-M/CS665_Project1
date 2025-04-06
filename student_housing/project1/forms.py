# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='First Name')
    last_name = forms.CharField(max_length=30, required=True, label='Last Name')
    email = forms.EmailField(required=True)
    country = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=False)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], required=False)

    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'country',
            'phone',
            'gender'
        ]
