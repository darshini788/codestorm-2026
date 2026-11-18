from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='feedbacks')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('resolved', 'Resolved')), default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
