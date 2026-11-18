from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    CATEGORY_CHOICES = (
        ('workshop', 'Workshop'),
        ('hackathon', 'Hackathon'),
        ('seminar', 'Seminar'),
        ('cultural', 'Cultural'),
        ('sports', 'Sports'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='workshop')
    poster = models.ImageField(upload_to='event_posters/', blank=True, null=True)
    date_time = models.DateTimeField()
    venue_or_link = models.CharField(max_length=255)
    registration_deadline = models.DateTimeField()
    participant_limit = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    is_cancelled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_registrations')
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'student')
