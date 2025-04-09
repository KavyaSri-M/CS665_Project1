from django.shortcuts import render

# Create your views here.


# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentSignUpForm

def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')  # Make sure you have a 'login' URL in your urls.py
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentSignUpForm()

    return render(request, 'signup.html', {'form': form})


from .forms import RoomForm

def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_success')  # After saving, redirect to success page or list
    else:
        form = RoomForm()
    return render(request, 'add_room.html', {'form': form})

def room_success(request):
    return render(request, 'room_success.html')
