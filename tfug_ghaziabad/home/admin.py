from django.contrib import admin
from .models import TeamMember, Achievement

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'position')
    search_fields = ('user__username', 'position')
    filter_horizontal = ('achievements',)

admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Achievement, AchievementAdmin)
