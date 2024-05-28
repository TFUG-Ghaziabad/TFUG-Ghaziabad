from django.shortcuts import render
from .models import TeamMember
from events.models import Speakers


def error_404_view(request, exception):
    return render(request, '404.html')

def admin_view(request):
    return render(request, 'admin.html')

def collaborations_view(request):
    return render(request, 'collaborations.html')

def contact_view(request):
    return render(request, 'contact.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def events_view(request):
    return render(request, 'events.html')

def find_us_view(request):
    return render(request, 'find_us.html')

def index_view(request):
    team_members = TeamMember.objects.all()
    speakers = Speakers.objects.all()
    return render(request, 'index.html', {'team_members': team_members, 'speakers': speakers})

def registration_view(request):
    return render(request, 'registration.html')

def speaker_view(request):
    return render(request, 'speaker.html')

def sponsor_view(request):
    return render(request, 'sponsor.html')

def team_registration_view(request):
    return render(request, 'team_registration.html')

def event_template_view(request):
    return render(request, 'event-template.html')

def launch_counter_view(request):
    return render(request, 'launch_counter.html')

def certificate_verification_view(request):
    return render(request, 'certificate/Certificate-Verification.html')

def social_page_view(request, page):
    return render(request, f'Social-Pages/{page}.html')
