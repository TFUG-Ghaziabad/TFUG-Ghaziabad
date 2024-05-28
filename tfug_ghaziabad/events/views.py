from django.shortcuts import render, get_object_or_404
from .models import Event, SpeakerEvent

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    speaker_events = SpeakerEvent.objects.filter(event=event)
    speakers = [speaker_event.speaker for speaker_event in speaker_events]
    return render(request, 'event_detail.html', {'event': event, 'speakers': speakers})