from django.urls import path
from . import views

urlpatterns = [
    path('', views.groups_list_view, name='groups_list'),
    path('join/<int:pk>/', views.request_join_group, name='request_join_group'),
    path('manage/<int:pk>/', views.manage_club_view, name='manage_club'),
    path('membership/<int:membership_id>/<str:action>/', views.club_membership_action, name='club_membership_action'),
]
