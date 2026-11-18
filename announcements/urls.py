from django.urls import path
from . import views

urlpatterns = [
    path('', views.announcements_list_view, name='announcements_list'),
]
