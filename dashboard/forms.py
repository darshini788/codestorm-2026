from django import forms
from django.contrib.auth.models import User
from events.models import Event
from groups.models import StudentGroup
from announcements.models import Announcement
from resources.models import Resource

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'category', 'description', 'poster', 'date_time', 'venue_or_link', 'registration_deadline', 'participant_limit']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Title'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'poster': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'date_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'venue_or_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seminar Hall / Google Meet URL'}),
            'registration_deadline': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'participant_limit': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Optional max seats'}),
        }

class GroupForm(forms.ModelForm):
    group_leader = forms.ModelChoiceField(
        queryset=User.objects.filter(is_superuser=False),
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    class Meta:
        model = StudentGroup
        fields = ['name', 'description', 'logo', 'group_leader']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Club / Group Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'priority', 'target_audience', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Announcement Title'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'target_audience': forms.Select(attrs={'class': 'form-select'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'category', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Resource Title'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
