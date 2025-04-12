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

from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'capacity', 'monthly_rent', 'floor', 'is_available']
        widgets = {
            'room_type': forms.TextInput(attrs={'class': 'validate'}),
            'capacity': forms.NumberInput(attrs={'class': 'validate'}),
            'monthly_rent': forms.NumberInput(attrs={'class': 'validate'}),
            'floor': forms.NumberInput(attrs={'class': 'validate'}),
            'is_available': forms.CheckboxInput(),
        }


from .models import MaintenanceRequest

class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['student', 'room', 'issue', 'status']
        widgets = {
            'student': forms.Select(attrs={'class': 'browser-default'}),
            'room': forms.Select(attrs={'class': 'browser-default'}),
            'issue': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'status': forms.Select(attrs={'class': 'browser-default'}),
        }

from .models import RoomAssignment

class RoomAssignmentForm(forms.ModelForm):
    class Meta:
        model = RoomAssignment
        fields = ['student', 'room', 'start_date']
        widgets = {
            'student': forms.Select(attrs={'class': 'browser-default'}),
            'room': forms.Select(attrs={'class': 'browser-default'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'validate'}),
        }
        
