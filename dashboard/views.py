from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.models import UserProfile
from events.models import Event, EventRegistration
from groups.models import StudentGroup, GroupMembership
from announcements.models import Announcement
from resources.models import Resource
from feedback.models import Feedback
from .forms import EventForm, GroupForm, AnnouncementForm, ResourceForm

def is_admin_user(user):
    if not user.is_authenticated:
        return False
    if user.is_superuser or user.is_staff:
        return True
    return hasattr(user, 'profile') and user.profile.role == 'admin'

def admin_login_view(request):
    if is_admin_user(request.user):
        return redirect('admin_dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and is_admin_user(user):
            login(request, user)
            messages.success(request, f"Welcome back, Admin {user.username}!")
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid credentials or you do not have Administrator access.")
    return render(request, 'dashboard/admin_login.html')

@login_required
def admin_dashboard(request):
    if not is_admin_user(request.user):
        messages.error(request, "Access Denied: Administrators only.")
        return redirect('home')

    context = {
        'total_students': User.objects.filter(is_superuser=False).count(),
        'total_events': Event.objects.count(),
        'total_groups': StudentGroup.objects.count(),
        'total_resources': Resource.objects.count(),
        'events': Event.objects.all().order_by('-created_at'),
        'groups': StudentGroup.objects.all().order_by('-created_at'),
        'announcements': Announcement.objects.all().order_by('-created_at'),
        'resources': Resource.objects.all().order_by('-uploaded_at'),
        'pending_memberships': GroupMembership.objects.filter(status='pending'),
        'users': User.objects.all().order_by('-date_joined'),
        'feedbacks': Feedback.objects.all().order_by('-submitted_at'),
        'event_form': EventForm(),
        'group_form': GroupForm(),
        'announcement_form': AnnouncementForm(),
        'resource_form': ResourceForm(),
    }
    return render(request, 'dashboard/admin_dashboard.html', context)

@login_required
def admin_add_event(request):
    if not is_admin_user(request.user):
        return redirect('home')
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            messages.success(request, "Event published successfully!")
        else:
            messages.error(request, f"Error adding event: {form.errors}")
    return redirect('admin_dashboard')

@login_required
def admin_delete_event(request, pk):
    if is_admin_user(request.user):
        get_object_or_404(Event, pk=pk).delete()
        messages.success(request, "Event deleted.")
    return redirect('admin_dashboard')

@login_required
def admin_add_group(request):
    if not is_admin_user(request.user):
        return redirect('home')
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.save()
            if group.group_leader and hasattr(group.group_leader, 'profile'):
                group.group_leader.profile.role = 'group_leader'
                group.group_leader.profile.save()
            messages.success(request, "Student group created successfully!")
    return redirect('admin_dashboard')

@login_required
def admin_add_announcement(request):
    if not is_admin_user(request.user):
        return redirect('home')
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            ann = form.save(commit=False)
            ann.created_by = request.user
            ann.save()
            messages.success(request, "Announcement posted!")
    return redirect('admin_dashboard')

@login_required
def admin_add_resource(request):
    if not is_admin_user(request.user):
        return redirect('home')
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            res = form.save(commit=False)
            res.uploaded_by = request.user
            res.save()
            messages.success(request, "Resource uploaded successfully!")
    return redirect('admin_dashboard')

@login_required
def admin_update_role(request, user_id):
    if is_admin_user(request.user) and request.method == 'POST':
        target_user = get_object_or_404(User, pk=user_id)
        new_role = request.POST.get('role')
        profile, _ = UserProfile.objects.get_or_create(user=target_user)
        profile.role = new_role
        profile.save()
        if new_role == 'admin':
            target_user.is_staff = True
            target_user.save()
        messages.success(request, f"Updated role for {target_user.username} to {new_role}.")
    return redirect('admin_dashboard')

@login_required
def admin_membership_action(request, membership_id, action):
    if is_admin_user(request.user):
        mem = get_object_or_404(GroupMembership, pk=membership_id)
        mem.status = 'approved' if action == 'approve' else 'rejected'
        mem.save()
        messages.success(request, f"Membership request {mem.status}.")
    return redirect('admin_dashboard')

@login_required
def admin_change_password(request):
    if not is_admin_user(request.user):
        return redirect('home')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Admin password changed successfully!")
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Please correct the password errors below.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/admin_change_password.html', {'form': form})

@login_required
def admin_delete_user(request, user_id):
    if is_admin_user(request.user):
        target = get_object_or_404(User, pk=user_id)
        if not target.is_superuser and target != request.user:
            target.delete()
            messages.success(request, "Unwanted student account removed.")
        else:
            messages.error(request, "Cannot delete primary administrator.")
    return redirect('admin_dashboard')
