# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentUpdateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'email', 'country', 'phone', 'gender']
        widgets = {
            'gender': forms.Select(attrs={'class': 'browser-default'}),
        }
    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        self.fields['gender'].label = ''

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Full Name')
    email = forms.EmailField(required=True)
    country = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=False)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], required=False,label="")

    class Meta:
        model = Student
        fields = [
            'first_name',
            'email',
            'country',
            'phone',
            'gender',
            'password1',
            'password2'
            
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        # Store phone number in username field
        user.username = self.cleaned_data['phone']
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.country = self.cleaned_data['country']
        user.gender = self.cleaned_data['gender']
        if commit:
            user.save()
        return user

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
        fields = ['room', 'issue', 'status']
        widgets = {
            'room': forms.Select(attrs={'class': 'browser-default'}),
            'issue': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'status': forms.Select(attrs={'class': 'browser-default'}),
        }

    def __init__(self, *args, **kwargs):
        super(MaintenanceRequestForm, self).__init__(*args, **kwargs)
        self.fields['room'].empty_label = "Select Room"
        self.fields['status'].empty_label = "Select Status"

from .models import RoomAssignment

class RoomAssignmentForm(forms.ModelForm):
    class Meta:
        model = RoomAssignment
        fields = ['room', 'start_date'] 
        widgets = {
            'room': forms.Select(attrs={'class': 'browser-default'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'validate'}),
        }

    def __init__(self, *args, **kwargs):
        super(RoomAssignmentForm, self).__init__(*args, **kwargs)
        self.fields['room'].empty_label = "Select Room"


