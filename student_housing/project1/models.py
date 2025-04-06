from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model extending AbstractUser
class Student(AbstractUser):
    country = models.CharField(max_length=100)  # Country of the student
    phone = models.CharField(max_length=15, blank=True, null=True)  # Phone (optional)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female')],
        blank=True,
        null=True
    )  # Gender choices

    # Optional: if you want to display full name easily
    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


# Rooms Table
class Room(models.Model):
    room_id = models.AutoField(primary_key=True)  # Auto increment primary key
    room_type = models.CharField(max_length=50)  # Room type (Single, Double, etc.)
    capacity = models.IntegerField()  # Capacity of room
    monthly_rent = models.FloatField()  # Monthly rent
    floor = models.IntegerField(blank=True, null=True)  # Floor (optional)
    is_available = models.BooleanField(default=True)  # Availability status

    def __str__(self):
        return f"Room {self.room_id} - {self.room_type}"


# Room Assignments Table
class RoomAssignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)  # Auto increment primary key
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Foreign key to Student
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Foreign key to Room
    start_date = models.DateField()  # Start date of assignment

    def __str__(self):
        return f"Assignment {self.assignment_id} - Student: {self.student.get_full_name()} Room: {self.room.room_id}"


# Maintenance Requests Table
class MaintenanceRequest(models.Model):
    request_id = models.AutoField(primary_key=True)  # Auto increment primary key
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Foreign key to Student
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Foreign key to Room
    issue = models.TextField()  # Description of issue
    status = models.CharField(
        max_length=20,
        default='Pending',
        choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')]
    )  # Status of request

    def __str__(self):
        return f"Request {self.request_id} - {self.issue[:30]}..."
