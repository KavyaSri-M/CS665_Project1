# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('student/signup/', views.student_signup, name='student_signup'),
    path('add-room/', views.add_room, name='add_room'),
    path('room-success/', views.room_success, name='room_success'),
]
