from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_list_view, name='events_list'),
    path('<int:pk>/', views.event_detail_view, name='event_detail'),
    path('<int:pk>/register/', views.register_event, name='register_event'),
]
