from django.contrib import admin
from Matches.models import Match, MatchPoints


@admin.register(Match)
class RiderAdmin(admin.ModelAdmin):
    list_display = (
        'home_team',
        'home_team_points',
        'guest_team_points',
        'guest_team',
        'date',
        'isFinished',
        'queue',
    )
    search_fields = ('home_team', 'guest_team', 'date', 'isFinished', 'queue', 'playoff')
    ordering = ('date',)


@admin.register(MatchPoints)
class RiderAdmin(admin.ModelAdmin):
    list_display = (
        'rider',
        'match',
        'runs',
        'bonuses',
        'team',
        'number',
        'joker_rider'
    )
    search_fields = ('rider', 'match', 'runs', 'bonuses', 'team', 'number',)
    ordering = ('rider',)
