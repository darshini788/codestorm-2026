from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    PRIORITY_CHOICES = (('normal', 'Normal'), ('important', 'Important'), ('urgent', 'Urgent'))
    TARGET_CHOICES = (('all', 'All Students'), ('CSE', 'CSE'), ('ECE', 'ECE'), ('ISE', 'ISE'), ('ME', 'ME'), ('CV', 'CV'), ('AIDS', 'AIDS'))
    title = models.CharField(max_length=200)
    content = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal')
    target_audience = models.CharField(max_length=50, choices=TARGET_CHOICES, default='all')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announcements')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
