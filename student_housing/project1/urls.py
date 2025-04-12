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
    path('edit-maintenance-request/<int:request_id>/', views.edit_maintenance_request, name='edit_maintenance_request'),
    path('maintenance-list/', views.maintenance_list, name='maintenance_list'),
    path('delete-maintenance-request/<int:request_id>/', views.delete_maintenance_request, name='delete_maintenance_request'),
    path('add-room-assignment/', views.add_room_assignment, name='add_room_assignment'),
    path('room-assignment-success/', views.room_assignment_success, name='room_assignment_success'),
    path('room-assignment-list/', views.room_assignment_list, name='room_assignment_list'),
    path('edit-room-assignment/<int:assignment_id>/', views.edit_room_assignment, name='edit_room_assignment'),
    path('delete-room-assignment/<int:assignment_id>/', views.delete_room_assignment, name='delete_room_assignment'),


]
