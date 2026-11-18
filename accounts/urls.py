from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
