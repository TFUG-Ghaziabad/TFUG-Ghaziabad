from django.contrib import admin
from .models import Event, Speakers, Topic, SpeakerEvent
from admin_interface.models import Theme

admin.site.unregister(Theme)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location')
    list_filter = ('date',)
    search_fields = ('title', 'location', 'description')
    prepopulated_fields = {'slug': ('title',)}  # Auto-populate slug field based on the title

admin.site.register(Event, EventAdmin)

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

    # Set verbose_name_plural for Speakers directly in the model's class
    verbose_name_plural = 'Speakers'

admin.site.register(Speakers, SpeakerAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    # Set verbose_name_plural for Topics directly in the model's class
    verbose_name_plural = 'Topics'

admin.site.register(Topic, TopicAdmin)

class SpeakerEventAdmin(admin.ModelAdmin):
    list_display = ('speaker', 'event',)
    search_fields = ('speaker__name', 'event__title',)
    filter_horizontal = ('topics',)

    # Set verbose_name_plural for SpeakerEvent directly in the model's class
    verbose_name_plural = 'Speaker Events'

admin.site.register(SpeakerEvent, SpeakerEventAdmin)
