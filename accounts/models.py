from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    DEPT_CHOICES = [
        ('CSE', 'Computer Science and Engineering'),
        ('ISE', 'Information Science and Engineering'),
        ('ECE', 'Electronics and Communication'),
        ('EEE', 'Electrical and Electronics'),
        ('ME', 'Mechanical Engineering'),
        ('CV', 'Civil Engineering'),
        ('AIML', 'Artificial Intelligence & Machine Learning'),
    ]

    SEM_CHOICES = [
        ('1st', '1st Semester'),
        ('2nd', '2nd Semester'),
        ('3rd', '3rd Semester'),
        ('4th', '4th Semester'),
        ('5th', '5th Semester'),
        ('6th', '6th Semester'),
        ('7th', '7th Semester'),
        ('8th', '8th Semester'),
    ]

    ROLE_CHOICES = [
        ('student', 'Student'),
        ('leader', 'Group Leader'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    usn = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    department = models.CharField(max_length=50, choices=DEPT_CHOICES, default='CSE')
    semester = models.CharField(max_length=10, choices=SEM_CHOICES, default='6th')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
