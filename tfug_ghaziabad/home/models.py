from django.db import models
from django.contrib.auth.models import User

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='team_member')
    image = models.ImageField(upload_to='static/team-avatars/')
    position = models.CharField(max_length=100)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    achievements = models.ManyToManyField(Achievement, blank=True)

    def __str__(self):
        return self.user.get_full_name()

