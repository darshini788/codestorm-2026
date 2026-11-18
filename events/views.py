from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, EventRegistration

def events_list_view(request):
    events = Event.objects.filter(is_cancelled=False).order_by('date_time')
    return render(request, 'events/events_list.html', {'events': events})

def event_detail_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    is_registered = False
    if request.user.is_authenticated:
        is_registered = EventRegistration.objects.filter(event=event, student=request.user).exists()
    return render(request, 'events/event_detail.html', {'event': event, 'is_registered': is_registered})

@login_required
def register_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    reg, created = EventRegistration.objects.get_or_create(event=event, student=request.user)
    if created:
        messages.success(request, f"Successfully registered for {event.title}!")
    else:
        messages.info(request, "You are already registered for this event.")
    return redirect('event_detail', pk=pk)
