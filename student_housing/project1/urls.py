# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('student/signup/', views.student_signup, name='student_signup'),
    path('add-room/', views.add_room, name='add_room'),
    path('room-success/', views.room_success, name='room_success'),
    path('edit-room/<int:room_id>/', views.edit_room, name='edit_room'),
    path('rooms/', views.room_list, name='room_list'),
    path('delete-room/<int:room_id>/', views.delete_room, name='delete_room'),
    path('add-maintenance-request/', views.add_maintenance_request, name='add_maintenance_request'),
    path('maintenance-success/', views.maintenance_success, name='maintenance_success'),
]
