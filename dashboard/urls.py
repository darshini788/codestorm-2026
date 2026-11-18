from django.urls import path
from . import views

urlpatterns = [
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('admin-portal/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-portal/add-event/', views.admin_add_event, name='admin_add_event'),
    path('admin-portal/delete-event/<int:pk>/', views.admin_delete_event, name='admin_delete_event'),
    path('admin-portal/add-group/', views.admin_add_group, name='admin_add_group'),
    path('admin-portal/add-announcement/', views.admin_add_announcement, name='admin_add_announcement'),
    path('admin-portal/add-resource/', views.admin_add_resource, name='admin_add_resource'),
    path('admin-portal/update-role/<int:user_id>/', views.admin_update_role, name='admin_update_role'),
    path('admin-portal/delete-user/<int:user_id>/', views.admin_delete_user, name='admin_delete_user'),
    path('admin-portal/membership/<int:membership_id>/<str:action>/', views.admin_membership_action, name='admin_membership_action'),
    path('admin-portal/change-password/', views.admin_change_password, name='admin_change_password'),
]
