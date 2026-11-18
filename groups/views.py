from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import StudentGroup, GroupMembership

def groups_list_view(request):
    groups = StudentGroup.objects.all().order_by('-created_at')
    user_memberships = {}
    if request.user.is_authenticated:
        for m in GroupMembership.objects.filter(student=request.user):
            user_memberships[m.group.id] = m.status
    return render(request, 'groups/groups_list.html', {
        'groups': groups,
        'user_memberships': user_memberships
    })

@login_required
def request_join_group(request, pk):
    group = get_object_or_404(StudentGroup, pk=pk)
    if group.group_leader == request.user:
        messages.warning(request, "You are the leader of this club.")
        return redirect('groups_list')
    membership, created = GroupMembership.objects.get_or_create(group=group, student=request.user)
    if created:
        messages.success(request, f"Membership request sent to {group.name} leader ({group.group_leader.username if group.group_leader else 'Admin'})!")
    else:
        messages.info(request, f"Your request status for {group.name} is: {membership.status}")
    return redirect('groups_list')

@login_required
def manage_club_view(request, pk):
    group = get_object_or_404(StudentGroup, pk=pk)
    if group.group_leader != request.user and not request.user.is_staff:
        messages.error(request, "Only the Group Leader can manage this club.")
        return redirect('groups_list')
    pending_requests = GroupMembership.objects.filter(group=group, status='pending')
    approved_members = GroupMembership.objects.filter(group=group, status='approved')
    return render(request, 'groups/manage_club.html', {
        'group': group,
        'pending_requests': pending_requests,
        'approved_members': approved_members
    })

@login_required
def club_membership_action(request, membership_id, action):
    mem = get_object_or_404(GroupMembership, pk=membership_id)
    if mem.group.group_leader != request.user and not request.user.is_staff:
        messages.error(request, "Permission denied.")
        return redirect('groups_list')
    if action == 'approve':
        mem.status = 'approved'
        mem.save()
        messages.success(request, f"Approved {mem.student.username} into {mem.group.name}.")
    elif action == 'reject':
        mem.status = 'rejected'
        mem.save()
        messages.warning(request, f"Rejected {mem.student.username}'s request.")
    elif action == 'remove':
        username = mem.student.username
        mem.delete()
        messages.success(request, f"Removed {username} from {mem.group.name}.")
    return redirect('manage_club', pk=mem.group.id)
