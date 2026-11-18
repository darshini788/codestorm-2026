from django.shortcuts import render
from .models import Announcement

def announcements_list_view(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, 'announcements/announcements_list.html', {'announcements': announcements})
