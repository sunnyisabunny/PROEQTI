from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Category
from .forms import EventForm

@login_required
def event_list(request):
    events = Event.objects.filter(user=request.user).order_by('date')
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            e = form.save(commit=False)
            e.user = request.user
            e.save()
            return redirect('event-list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form, "event": None})

@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form, 'event': event})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('event-list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})
