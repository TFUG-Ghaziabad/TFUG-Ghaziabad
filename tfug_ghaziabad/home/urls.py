from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin'),
    path('collaborations/', views.collaborations_view, name='collaborations'),
    path('contact/', views.contact_view, name='contact'),
    path('find-us/', views.find_us_view, name='find_us'),
    path('', views.index_view, name='index'),
    path('registration/', views.registration_view, name='registration'),
    path('speaker/', views.speaker_view, name='speaker'),
    path('sponsor/', views.sponsor_view, name='sponsor'),
    path('call_for_volunteers/', views.volunteer_view, name='volunteer'),
    path('team-registration/', views.team_registration_view, name='team_registration'),
    path('launch-counter/', views.launch_counter_view, name='launch_counter'),
    path('certificate/verification/', views.certificate_verification_view, name='certificate_verification'),
    path('social-pages/<str:page>/', views.social_page_view, name='social_page'),
    path('studyplanner/', views.studyplanner, name='studyplanner'),
    
    
    
    
    path('calander2025/', views.calander, name='calander'),
]

# Custom error handling
handler404 = 'home.views.error_404_view'
