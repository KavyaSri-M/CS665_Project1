from django.shortcuts import render

# Create your views here.


# views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import login


def home(request):
    return render(request,'home.html')

def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            messages.success(request, 'Account created successfully!')
            return redirect('profile') 
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentSignUpForm()

    return render(request, 'signup.html', {'form': form})


def student_profile(request):
    student = request.user  # Current logged-in student

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = StudentUpdateForm(instance=student)

    context = {
        'student': student,
        'form': form,
    }

    return render(request, 'profile.html', context)


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



def edit_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')  # Redirect to room list page after saving
    else:
        form = RoomForm(instance=room)

    return render(request, 'edit_room.html', {'form': form, 'room': room})


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms_list.html', {'rooms': rooms})


def delete_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    if request.method == 'POST':
        room.delete()
        return redirect('room_list')  # Redirect to room list after deletion

    return render(request, 'delete_room.html', {'room': room})


from .forms import MaintenanceRequestForm

def add_maintenance_request(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            maintenance_request = form.save(commit=False)
            maintenance_request.student = request.user  # set the current logged-in student
            maintenance_request.save()
            messages.success(request, 'Maintenance request submitted successfully!')
            return redirect('maintenance_success')  #   Redirect to success page
    else:
        form = MaintenanceRequestForm()
    return render(request, 'add_maintenance_request.html', {'form': form})

def maintenance_success(request):
    return render(request, 'maintenance_success.html')


def edit_maintenance_request(request, request_id):
    maintenance_request = get_object_or_404(MaintenanceRequest, pk=request_id)

    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST, instance=maintenance_request)
        if form.is_valid():
            maintence_obj = form.save(commit=False)
            maintence_obj.student = request.user
            form.save()
            return redirect('maintenance_list')  # Redirect to list page or success page
    else:
        form = MaintenanceRequestForm(instance=maintenance_request)

    return render(request, 'edit_maintenance_request.html', {'form': form, 'maintenance_request': maintenance_request})

def delete_maintenance_request(request, request_id):
    maintenance_request = get_object_or_404(MaintenanceRequest, pk=request_id)

    if request.method == 'POST':
        maintenance_request.delete()
        return redirect('maintenance_list')  # After deletion, redirect to list

    return render(request, 'confirm_delete_maintenance.html', {'maintenance_request': maintenance_request})

def maintenance_list(request):
    maintenance_requests = MaintenanceRequest.objects.all()
    return render(request, 'maintenance_list.html', {'maintenance_requests': maintenance_requests})


from .forms import RoomAssignmentForm

def add_room_assignment(request):
    if request.method == 'POST':
        form = RoomAssignmentForm(request.POST)
        if form.is_valid():
            room_assignment = form.save(commit=False)
            room_assignment.student = request.user  # Set the current logged-in student
            room_assignment.save()
            room_assignment.room.is_available = False
            room_assignment.room.save()
            messages.success(request, 'Room assigned successfully!')
            return redirect('room_assignment_list')  # Redirect to list page or success page
    else:
        form = RoomAssignmentForm()

    return render(request, 'add_room_assignment.html', {'form': form})

def room_assignment_list(request):
    student = request.user
    assignments = RoomAssignment.objects.filter(student=student)
    return render(request, 'room_assignment_list.html', {'assignments': assignments})


def edit_room_assignment(request, assignment_id):
    assignment = get_object_or_404(RoomAssignment, pk=assignment_id)

    if request.method == 'POST':
        form = RoomAssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('room_assignment_list')
    else:
        form = RoomAssignmentForm(instance=assignment)

    return render(request, 'edit_room_assignment.html', {'form': form, 'assignment': assignment})

def delete_room_assignment(request, assignment_id):
    assignment = get_object_or_404(RoomAssignment, pk=assignment_id)

    if request.method == 'POST':
        assignment.delete()
        return redirect('room_assignment_list')

    return render(request, 'confirm_delete_room_assignment.html', {'assignment': assignment})


