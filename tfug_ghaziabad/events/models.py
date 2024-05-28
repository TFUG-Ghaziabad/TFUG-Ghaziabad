from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify

class Event(models.Model):
    # Existing fields
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    closing_time = models.TimeField()
    location = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')
    registration_link = models.URLField(blank=True)
    collaboration_link = models.URLField(blank=True)
    sponsorship_link = models.URLField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    # Define event statuses as choices
    STATUS_CHOICES = [
        ('UPCOMING', 'Upcoming'),
        ('ONGOING', 'Ongoing'),
        ('ENDED', 'Ended'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='UPCOMING')
    speakers = models.ManyToManyField('Speakers', related_name='events', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_status(self):
        """
        Determine the status of the event based on the current date and time.
        """
        now = timezone.now()
        event_datetime = timezone.datetime.combine(self.date, self.time)
        closing_datetime = timezone.datetime.combine(self.date, self.closing_time)

        if now < event_datetime:
            self.status = 'UPCOMING'
        elif now < closing_datetime:
            self.status = 'ONGOING'
        else:
            self.status = 'ENDED'

        return self.status

@receiver(post_save, sender=Event)
def update_event_status(sender, instance, **kwargs):
    """
    Automatically update the status of the event on the day of the event and the next day.
    """
    today = timezone.localdate()
    event_date = instance.date

    # Check if today is the event day or the next day
    if today == event_date or today == event_date + timezone.timedelta(days=1):
        instance.get_status()
        instance.save()

class Speakers(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='speakers/')
    description = models.TextField()
    email = models.EmailField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SpeakerEvent(models.Model):
    speaker = models.ForeignKey(Speakers, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic, related_name='speaker_events')

    def __str__(self):
        return f"{self.speaker.name} at {self.event.title}"