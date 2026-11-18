from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import StudentRegistrationForm, UserProfileEditForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.usn = form.cleaned_data['usn']
            profile.phone_number = form.cleaned_data['phone_number']
            profile.address = form.cleaned_data['address']
            profile.department = form.cleaned_data['department']
            profile.semester = form.cleaned_data['semester']
            if form.cleaned_data.get('avatar'):
                profile.avatar = form.cleaned_data['avatar']
            profile.role = 'student'
            profile.save()

            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('student_dashboard')
        else:
            messages.error(request, f"Registration failed: {form.errors}")
    else:
        form = StudentRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def student_dashboard(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/student_dashboard.html', {'profile': profile})

@login_required
def edit_profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            request.user.first_name = request.POST.get('first_name', request.user.first_name)
            request.user.last_name = request.POST.get('last_name', request.user.last_name)
            request.user.email = request.POST.get('email', request.user.email)
            request.user.save()
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('student_dashboard')
    else:
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
        form = UserProfileEditForm(instance=profile, initial=initial_data)
    return render(request, 'accounts/edit_profile.html', {'form': form})
