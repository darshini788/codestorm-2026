from django.db import models
from django.contrib.auth.models import User

class StudentGroup(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    logo = models.ImageField(upload_to='group_logos/', blank=True, null=True)
    group_leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='led_groups')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GroupMembership(models.Model):
    STATUS_CHOICES = (('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'))
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, related_name='memberships')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_memberships')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    requested_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('group', 'student')
