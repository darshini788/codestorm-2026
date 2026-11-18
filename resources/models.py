from django.db import models
from django.contrib.auth.models import User

class Resource(models.Model):
    CATEGORY_CHOICES = (('notes', 'Lecture Notes'), ('syllabus', 'Syllabus'), ('qp', 'Previous Question Papers'), ('timetable', 'Timetable'), ('form', 'Official Form'), ('placement', 'Placement & Internship'))
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='notes')
    file = models.FileField(upload_to='resources/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_resources')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
